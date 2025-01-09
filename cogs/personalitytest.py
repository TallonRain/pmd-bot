import discord
from discord.ext import commands, bridge

from main import DEBUG_MODE

class QuizButton(discord.ui.Button):
    def __init__(self, label: str, custom_id: str):
        super().__init__(label=label, style=discord.ButtonStyle.primary, custom_id=custom_id)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"You clicked {self.label}!", ephemeral=True)
        await interaction.message.edit(
            view=None
        )

class InteractiveButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(QuizButton(label="Option 1", custom_id="option_1"))
        self.add_item(QuizButton(label="Option 2", custom_id="option_2"))




class PersonalityTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(description="Welcome to the world inhabited only by Pokémon...")
    async def pmd(self, ctx):
        user = ctx.author
        user_id = user.id # needed to maintain context of who used the command so we can save their results later
        result_score = {} # key-value pair to associate accumulated points between different natures as the user
        # answers questions, then we tally the results and fetch the highest value as the result of the test
        answer_a = "A"
        answer_b = "B"
        answer_c = "C"
        answer_d = "D"

        test_question = "You've been asked to do a difficult task. What will you do?"
        question_number = "Question 1"

        embed = discord.Embed(
            title="PMD Bot",
            description="This is the portal that leads to the world inhabited only by Pokémon.\nBeyond this gateway, "
                        "many new adventures and fresh experiences await your arrival!\nBefore you depart for the "
                        "adventure, you must answer some questions.\nBe truthful when you answer them!\nNow, "
                        "are you ready?\nThen...let the questions begin!",
            color=discord.Colour.blurple())
        embed.add_field(name=question_number, value=test_question, inline=False)
        embed.add_field(name="A", value="Do nothing.", inline=False)
        embed.add_field(name="B", value="Do something.", inline=False)
        embed.add_field(name="C", value="Do something else.", inline=False)
        embed.add_field(name="D", value="Cry.", inline=False)
        embed.set_image(url="https://i.imgur.com/DaO700N.gif")

        view = discord.ui.View()
        view.add_item(QuizButton(label="Answer A", custom_id=f"pmd_question_{answer_a}"))
        view.add_item(QuizButton(label="Answer B", custom_id=f"pmd_question_{answer_b}"))
        view.add_item(QuizButton(label="Answer C", custom_id=f"pmd_question_{answer_c}"))
        view.add_item(QuizButton(label="Answer D", custom_id=f"pmd_question_{answer_d}"))
        await ctx.respond(embed=embed, ephemeral=True, view=view)
        if not DEBUG_MODE:
            pass


def setup(bot):
    bot.add_cog(PersonalityTest(bot))
