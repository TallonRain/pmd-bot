from collections.abc import Awaitable, Callable
import discord
from discord.ext import commands
import string
from typing import Optional
from .data import load_questions, load_pokemon, load_natures
from utils.testutils import generate_unique_random_numbers

long_description = "This is the portal that leads to the world inhabited only by Pokémon. Beyond this gateway, " \
                   "many new adventures and fresh experiences await your arrival! Before you depart for the " \
                   "adventure, you must answer some questions. Be truthful when you answer them! Now, " \
                   "are you ready? Then...let the questions begin!"

# prepare the personality test data
questions = load_questions()
pokemon_map = load_pokemon()
natures = load_natures()


class QuizButton(discord.ui.Button):
    def __init__(self, callback: Callable[[str, discord.Interaction], Awaitable[None]], label: str, custom_id: str):
        self.user_callback = callback
        super().__init__(label=label, style=discord.ButtonStyle.secondary, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        await self.user_callback(self.custom_id, interaction)


# constructs the internal state of the personality test session to track progress
class QuizState:
    def __init__(self, user_id: int, question_list: list[int]):
        self.user_id = user_id
        self.question_list = question_list
        self.current_question_index = 0
        self.scores: dict[string, int] = {}
        self.last_message: Optional[discord.Interaction] = None

    def accumulate_scores(self, scores: dict[str, int]):
        for nature, score in scores.items():
            self.scores[nature] = self.scores.get(nature, 0) + score

    @property
    def top_nature(self) -> str:
        return max(self.scores.items(), key=lambda x: x[1])[0]


class PersonalityTest(commands.Cog):
    def __init__(self, bot: 'discord.ext.commands.Bot'):
        self.bot = bot
        self.ongoing_quizzes: dict[int, QuizState] = {}

    # Beginning of the /pmd command
    @discord.slash_command(description="Welcome to the world inhabited only by Pokémon...")
    async def pmd(self, ctx: discord.ApplicationContext):
        question_numbers = generate_unique_random_numbers(10, 0, 63)  # select ten questions from the pool
        user_id = ctx.author.id
        state = QuizState(user_id, question_numbers)
        self.ongoing_quizzes[user_id] = state

        embed, view = self.generate_response_parts(state)
        state.last_message = await ctx.respond(embed=embed, ephemeral=True, view=view)

    # Fetch what question the user just responded to in their session, score it, check if we have more, and then set
    # up and send the next question if we do. Else, end the quiz.
    async def button_callback(self, original_user_id: int, custom_id: str, interaction: discord.Interaction):
        state = self.ongoing_quizzes[original_user_id]
        real_question_number = state.question_list[state.current_question_index]
        question = questions[real_question_number]
        selected_answer = question.answers[int(custom_id)]
        state.accumulate_scores(selected_answer.natures)

        if state.current_question_index >= len(state.question_list) - 1:
            await self.end_quiz(state, interaction)
            return

        state.current_question_index += 1
        embed, view = self.generate_response_parts(state)
        await state.last_message.edit_original_response(embed=embed, view=view)
        await interaction.response.defer(invisible=True)

    # End the quiz, terminate the session, send final results
    async def end_quiz(self, state: QuizState, interaction: discord.Interaction):
        nature = state.top_nature
        pokemon = pokemon_map[nature]
        nature_desc = natures[nature]

        embed = discord.Embed(
            title="PMD Bot",
            color=discord.Color.blurple(),
            description=nature_desc
        )
        embed.add_field(name="", value=f"Would be a {pokemon[0]} or {pokemon[1]}!")
        await state.last_message.edit_original_response(embed=embed, view=discord.ui.View())
        await interaction.response.defer(invisible=True)
        del self.ongoing_quizzes[state.user_id]

    # Generate the Discord embeds which convey the series of questions to the user
    def generate_response_parts(self, state: QuizState) -> (discord.Embed, discord.ui.View):
        view = discord.ui.View()
        embed = discord.Embed(
            title="PMD Bot",
            color=discord.Colour.blurple(),
        )
        if state.current_question_index == 0:
            embed.description = long_description

        question = questions[state.question_list[state.current_question_index]]
        embed.add_field(name=f"Question {state.current_question_index + 1}", value=question.text, inline=False)
        for i, answer in enumerate(question.answers):
            embed.add_field(name=string.ascii_uppercase[i], value=answer.text, inline=True)
            view.add_item(QuizButton(
                lambda custom_id, interaction: self.button_callback(state.user_id, custom_id, interaction),
                label=string.ascii_uppercase[i],
                custom_id=str(i)))
            if i % 2 == 1:
                embed.add_field(name="", value="", inline=False)  # blank line for formatting reasons
        embed.set_image(url="https://i.imgur.com/DaO700N.gif")

        return embed, view


def setup(bot):
    bot.add_cog(PersonalityTest(bot))
