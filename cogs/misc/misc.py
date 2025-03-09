import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")
    
    @commands.command()
    async def repeat(self, ctx, *, message):
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Misc(bot))