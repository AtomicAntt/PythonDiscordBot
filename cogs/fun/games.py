import discord
import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def flip(self, ctx):
        choices = ["Heads", "Tails"]
        await ctx.send(f'{random.choice(choices)}')
    
    # This is my personal command
    @commands.command(name="8ball")
    async def eightball(self, ctx):
        good = ["Yep.", "It is certain.", "Without a doubt.", "Most likely.", "I guarantee it."]
        bad = ["No.", "Definitely not.", "Very unlikely.", "I don't think so." ]

        response_type = random.choice([good, bad])
        response = random.choice(response_type)

        await ctx.send(f'{ctx.author.mention} 🎱 {response}')
    
    @commands.command()
    async def guess(self, ctx):
        number = random.randint(1, 10)
        guesses = 3
        await ctx.send(f'{ctx.author.mention} I am thinking of a number from 1-10, try and guess it! Guesses left: **{guesses}**')

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigit()

        while guesses > 0:
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=30.0)
                guess = int(msg.content)
                if guess == number:
                    await ctx.send(f'{ctx.author.mention} Congratulations, you won! The number I was thinking of was **{number}**! 🎊')
                    break
                elif guess < number:
                    guesses -= 1
                    await ctx.send(f'{ctx.author.mention} The number **{guess}** is too low, try again! You have **{guesses}** guesses remaining!')
                elif guess > number:
                    guesses -=1
                    await ctx.send(f'{ctx.author.mention} The number **{guess}** is too high, try again! You have **{guesses}** guesses remaining!')
                
                if guesses <= 0:
                    await ctx.send(f'{ctx.author.mention} Sorry, you have lost the game! The number I was thinking of was **{number}**!')
                    break
                
            except TimeoutError:
                await ctx.send(f'{ctx.author.mention} Took too long to respond, the number I was thinking of is **{number}**!')
                break

async def setup(bot):
    await bot.add_cog(Games(bot))