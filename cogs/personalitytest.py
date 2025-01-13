import json
import discord
from discord.ext import commands

from main import DEBUG_MODE
from utils.testutils import fetch_question, generate_unique_random_numbers

long_description = "This is the portal that leads to the world inhabited only by Pokémon.\nBeyond this gateway, " \
                   "many new adventures and fresh experiences await your arrival!\nBefore you depart for the " \
                   "adventure, you must answer some questions.\nBe truthful when you answer them!\nNow, " \
                   "are you ready?\nThen...let the questions begin!"

# prepare the personality test data
with open('quiz/natures-en.json') as f:
    natures = json.load(f)
with open('quiz/questions-en.json') as f:
    questions = json.load(f)
with open('quiz/naturetopokemon-en.json') as f:
    nature_to_pokemon = json.load(f)
with open('quiz/naturedescription-en.json') as f:
    nature_description = json.load(f)


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
            question_number = "Question " + str(count)
            if loop_iteration == 0:
                embed = discord.Embed(
                    title="PMD Bot",
                    description=long_description,
                    color=discord.Colour.blurple(),
                )
            else:
                embed = discord.Embed(
                    title="PMD Bot",
                    color=discord.Colour.blurple(),
                )

            embed.add_field(name=question_number, value=fetch_question(questions_list[count]), inline=False)
            embed.add_field(name="A", value="Do nothing.", inline=True)
            embed.add_field(name="B", value="Do something.", inline=True)
            embed.add_field(name="", value="", inline=False) # blank line for formatting reasons
            embed.add_field(name="C", value="Do something else.", inline=True)
            embed.add_field(name="D", value="Cry.", inline=True)
            embed.set_image(url="https://i.imgur.com/DaO700N.gif")

            view = discord.ui.View()

            view.add_item(QuizButton(label="A", custom_id="A"))
            view.add_item(QuizButton(label="B", custom_id="B"))
            view.add_item(QuizButton(label="C", custom_id="C"))
            view.add_item(QuizButton(label="D", custom_id="D"))
            await ctx.respond(embed=embed, ephemeral=True, view=view)
            loop_iteration += 1
            if not DEBUG_MODE:
                pass


def setup(bot):
    bot.add_cog(PersonalityTest(bot))
