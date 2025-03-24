import discord
from discord.ext import commands
import random

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

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def add(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)

@bot.command()
async def addall(ctx, *args: int):
    total = 0
    for num in args:
        total += num
    await ctx.send(total)

@bot.command()
async def repeat(ctx, *, message):
    await ctx.send(message)

@bot.command()
async def dm(ctx):
    await ctx.author.send("Hello!")

@bot.command()
async def reply(ctx):
    await ctx.reply("Hello!")

@bot.command()
async def react(ctx):
    await ctx.message.add_reaction('✨')

@bot.command()
async def flip(ctx):
    choices = ["Heads", "Tails"]
    await ctx.send(f'{random.choice(choices)}')


@bot.command(name="8ball")
async def eightball(ctx):
    good = ["Yep.", "It is certain.", "Without a doubt.", "Most likely.", "I guarantee it."]
    bad = ["No.", "Definitely not.", "Very unlikely.", "I don't think so." ]

    response_type = random.choice([good, bad])
    response = random.choice(response_type)

    await ctx.send(f'{ctx.author.mention} 🎱 {response}')

@bot.command()
async def respond(ctx):
    await ctx.send("You have 5 seconds to respond!")

    def check(m):
        return m.author == ctx.author
    try:
        await bot.wait_for("message", check=check, timeout=5.0)
        await ctx.send("Thank you for responding!")
    except TimeoutError:
        await ctx.send("5 seconds has passed, it is now too late to respond!")

@bot.command()
async def reactionadd(ctx):
    message = await ctx.send("React ✅ to this message to confirm!")
    await message.add_reaction("✅")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == "✅"
    try:
        await bot.wait_for('reaction_add', check=check, timeout=10.0)
        await ctx.send("Thank you for confirming!")
    except TimeoutError:
        await ctx.send("10 seconds have passed, it is now too late to confirm!")

bot.run(bot_token)