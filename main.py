import os
import discord
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv
import fixup
import datetime
from zoneinfo import ZoneInfo
import random

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PMD_CHANNEL_ID = int(os.getenv('PMD_CHANNEL_ID'))
DEBUG_MODE = bool(int(os.getenv('DEBUG_MODE')))
FILE_STORAGE = os.getenv('FILE_STORAGE')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=discord.Game("with spare Time Gears"))
    if DEBUG_MODE:
        print("DEBUG MODE ENABLED")

# fixup addresses a fatal SSL & authentication bug in Discord.py
fixup.run(bot, DISCORD_TOKEN)

