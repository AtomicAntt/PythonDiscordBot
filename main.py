import discord

# ENV FILE (to hide token) ==================================
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("DISCORD_BOT_TOKEN")
# ENV FILE (to hide token) ==================================

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
    status = discord.CustomActivity(name="your text")
    await client.change_presence(status=discord.Status.online, activity=status)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(';hello'):
        await message.channel.send('Hello!')

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send("Someone just added a reaction to a message!")

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} just editted a message!\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )

client.run(bot_token)