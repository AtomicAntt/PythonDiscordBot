import discord

# ENV FILE (to hide token) ==================================
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("DISCORD_BOT_TOKEN")
# ENV FILE (to hide token) ==================================

intents = discord.Intents.default()
intents.message_content = True

status = discord.CustomActivity(name="your text")
client = discord.Client(intents=intents, activity=status)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$reply'):
        await message.reply('Hi!')
    
    if message.content.startswith('$mention'):
        await message.channel.send(message.author.mention)

    if message.content.startswith('$dm'):
        await message.author.send('Hello!')

    if message.content.startswith('$react'):
        await message.add_reaction('✨')

@client.event
async def on_reaction_add(reaction, user):
    print(f'{user} just added a reaction to a message! This was the reaction: {reaction}')

@client.event
async def on_message_delete(message):
    print(f'{message.author} just had their message deleted: {message.content}')

@client.event
async def on_message_edit(before, after):
    print(f'{before.author} just edited a message!\nBefore: {before.content}\nAfter: {after.content}')

@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)

    # Since fetch_message and fetch_user are coroutines, we need to await.
    message = await channel.fetch_message(payload.message_id)
    user = await client.fetch_user(payload.user_id)

    print(f'{user} just added a reaction to a message!\nThe message reacted to:\n**{message.content}**\nThe reaction was: {payload.emoji}')

client.run(bot_token)