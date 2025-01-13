import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import fixup
import pathlib

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DEBUG_MODE = bool(int(os.getenv('DEBUG_MODE')))
FILE_STORAGE = os.getenv('FILE_STORAGE')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents, application_commands=True)


# iterate through all the cogs and load them into the bot
def load_cogs():
    numofcogs = 0
    for filepath in pathlib.Path('./cogs').iterdir():
        if filepath.suffix == '.py':
            bot.load_extension(f'cogs.{filepath.stem}')
            numofcogs += 1
        elif (filepath / '__init__.py').exists():
            bot.load_extension(f'cogs.{filepath.name}')
            numofcogs += 1
    print(f"{numofcogs} cog(s) loaded.")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game("with spare Time Gears"))
    if DEBUG_MODE:
        print("\n!!DEBUG MODE ENABLED!!\n")


load_cogs()
# fixup addresses a fatal SSL & authentication bug in Discord.py
# TODO: Is this still necessary for Pycord?
fixup.run(bot, DISCORD_TOKEN, DEBUG_MODE)
