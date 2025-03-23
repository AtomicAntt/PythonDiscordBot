import discord
from discord.ext import commands

# ENV FILE (to hide token) ==================================
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("DISCORD_BOT_TOKEN")
# ENV FILE (to hide token) ==================================

intents = discord.Intents.default()
intents.message_content = True

status = discord.CustomActivity(name="your text")
bot = commands.Bot(command_prefix='$', intents=intents, activity=status)

cogs = ["cogs.fun.games", "cogs.fun.apis", "cogs.math.math", "cogs.misc.misc"]

@bot.event
async def on_ready():
    for cog in cogs:
        print(f'Loading cog {cog}')
        await bot.load_extension(cog)

    print(f'We have logged in as {bot.user}')

bot.run(bot_token)