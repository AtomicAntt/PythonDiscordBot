import discord
import aiohttp
from discord.ext import commands

# https://docs.aiohttp.org/en/stable/
# https://dictionaryapi.dev/
# https://stackoverflow.com/questions/68888133/error-implementing-free-dictionary-api-in-discord-py

class Apis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def define(self, ctx, word):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}') as response:
                if response.status == 200:
                    info = await response.json()
                else:
                    await ctx.send(f'No definition found for **{word}**')
                    return
                
        await ctx.send(info[0]['meanings'][0]['definitions'][0]['definition'])

async def setup(bot):
    await bot.add_cog(Apis(bot))