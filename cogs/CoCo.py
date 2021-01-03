import discord
import asyncio
from discord.ext import commands

import random

class CoCo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="안녕")
    async def hello(self, ctx):
        await ctx.send("안녕하세요 " + ctx.message.author.mention + " 님!")

    @commands.command(name="코코야")
    async def HeyYou(self, ctx):
        CoCoResponse = ["네?", "뭐", "왜", "ㅇㅇ?", "누가 불렀니", "아 왜 불러ㅡㅡ"]
        
        await ctx.send(CoCoResponse[random.randint(0, 6)])

    @commands.command(name="짖어")
    async def bark(self, ctx):
        CoCoBark = ["크르릉...", "뀨웅?", "왈왈!", "멍멍!"]
        
        await ctx.send(CoCoBark[random.randint(0, 3)])

def setup(bot):
    bot.add_cog(CoCo(bot))