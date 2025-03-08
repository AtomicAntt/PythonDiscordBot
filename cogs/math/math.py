import discord
from discord.ext import commands

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def add(self, ctx, *args: int):
        total = 0
        for num in args:
            total += num
        await ctx.send(total)

async def setup(bot):
    await bot.add_cog(Math(bot))