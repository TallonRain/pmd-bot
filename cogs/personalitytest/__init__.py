import discord
from discord.ext import commands
import string

from main import DEBUG_MODE
from .data import load_questions
from utils.testutils import generate_unique_random_numbers

long_description = "This is the portal that leads to the world inhabited only by Pokémon.\nBeyond this gateway, " \
                   "many new adventures and fresh experiences await your arrival!\nBefore you depart for the " \
                   "adventure, you must answer some questions.\nBe truthful when you answer them!\nNow, " \
                   "are you ready?\nThen...let the questions begin!"

# prepare the personality test data
questions = load_questions()


class QuizButton(discord.ui.Button):
    # The button needs to be given labels for A, B, C, D answers and the custom_id should be the same
    def __init__(self, label: str, custom_id: str):
        super().__init__(label=label, style=discord.ButtonStyle.secondary, custom_id=custom_id)

    # core logic should go here
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"You clicked {self.label}!", ephemeral=True)


class PersonalityTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Welcome to the world inhabited only by Pokémon...")
    async def pmd(self, ctx):
        # needed to maintain context of who used the command so we can respond to them specifically and save their
        # results later
        user = ctx.author
        user_id = user.id
        count = 0
        loop_iteration = 0
        questions_list = generate_unique_random_numbers(10, 1, 64) # select ten questions from the pool

        while count < 3:  #TODO: Change this limiter when implementation is further progressed
            count += 1
            view = discord.ui.View()
            embed = discord.Embed(
                title="PMD Bot",
                color=discord.Colour.blurple(),
            )
            if loop_iteration == 0:
                embed.description = long_description

            question = questions[count]
            embed.add_field(name=f"Question {count}", value=question.text, inline=False)
            for i, answer in enumerate(question.answers):
                embed.add_field(name=string.ascii_uppercase[i], value=answer.text, inline=True)
                view.add_item(QuizButton(label=string.ascii_uppercase[i], custom_id=str(i)))
                if i % 2 == 1:
                    embed.add_field(name="", value="", inline=False)  # blank line for formatting reasons
            embed.set_image(url="https://i.imgur.com/DaO700N.gif")

            await ctx.respond(embed=embed, ephemeral=True, view=view)
            loop_iteration += 1
            if not DEBUG_MODE:
                pass


def setup(bot):
    bot.add_cog(PersonalityTest(bot))
