import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    status = discord.CustomActivity(name="your text")
    await client.change_presence(status=discord.Status.online, activity=status)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    await client.process_commands(message)

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send("Someone just added a reaction to a message!")

@client.command()
async def add(ctx, arg1: int, arg2: int):
    await ctx.send(str(arg1 + arg2))

client.run(bot_token)