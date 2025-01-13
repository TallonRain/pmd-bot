import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import fixup
import datetime
from zoneinfo import ZoneInfo

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PMD_CHANNEL_ID = int(os.getenv('PMD_CHANNEL_ID'))
DEBUG_MODE = bool(int(os.getenv('DEBUG_MODE')))
FILE_STORAGE = os.getenv('FILE_STORAGE')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents, application_commands=True)

# Set Time Zone
pacific_timezone = ZoneInfo("America/Los_Angeles")


#TODO: Remove and build a standardized help panel in its own module
async def generate_embed():
    embed = discord.Embed(url="https://github.com/TallonRain/pmd-bot", title="Source Code",
                          colour=discord.Colour.default())
    embed.add_field(name="Pokémon Mystery Dungeon Bot", value="")
    embed.add_field(name="Field 2", value="Value 2")
    embed.timestamp = datetime.datetime.now(pacific_timezone)
    embed.set_footer(text="This is a footer.")
    return embed


# iterate through all the cogs and load them into the bot
def load_cogs():
    numofcogs = 0
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
            numofcogs += 1
    print(f"{numofcogs} cog(s) loaded.")


#TODO: remove from the main module
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == PMD_CHANNEL_ID and message.content.startswith("!pmd"):
        await message.channel.send("Try using /pmd instead!")
        embed_object = await generate_embed()
        await message.channel.send(embed=embed_object)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!\nLogin time is {datetime.datetime.now(pacific_timezone)}')
    await bot.change_presence(activity=discord.Game("with spare Time Gears"))
    if DEBUG_MODE:
        print("\n!!DEBUG MODE ENABLED!!\n")


load_cogs()
# fixup addresses a fatal SSL & authentication bug in Discord.py
#TODO: Is this still necessary for Pycord?
fixup.run(bot, DISCORD_TOKEN, DEBUG_MODE)
