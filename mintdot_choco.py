import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

token = 'NDUzNDM5NTQwMTg3ODg5Njg1.DfpOCg.tkNCrOVrWvMP8Mrh9ejW8-QwojE'

bot = commands.Bot(command_prefix='!!')

@bot.event
async def on_ready():
    print("CHOCO BOT IS READY")
    print("BOT NAME: " + bot.user.name)
    print("BOT ID: " + str(bot.user.id))
    activity = discord.Game(name="!!help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    # await bot.change_presence(game=discord.Game(name="!!"))

@bot.command(pass_context=True, name="초코")
async def co(ctx):
    """
    하루에 한 번쯤은 초코를 불러줘야 하지 않겠는가?
    """
    embed = discord.Embed(title="Let's co's time.")
    embed.set_author(name="1DAY 1CO", icon_url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    embed.set_image(url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    embed.set_footer(text="co is best dog", icon_url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    await ctx.send(embed=embed)

@bot.command(pass_context=True, name="좆망겜왜해요")
async def wtf(ctx):
    """
    트위치/밈
    """
    await ctx.send("아니 그거 재밌다니깐요?")

@bot.command(pass_context=True, name="메이플왜해요")
async def maple(ctx):
    """
    트위치/밈
    """
    await ctx.send("아니 그거 재밌다니깐요?")

@bot.command(pass_context=True, name="오버워치왜해요")
async def overwatch(ctx):
    """
    트위치/밈
    """
    await ctx.send("아니 그거 재밌다니깐요?")

@bot.command(pass_context=True, name="와우왜해요")
async def wow(ctx):
    """
    트위치/밈
    """
    await ctx.send("록타 오가르!")

bot.run(token)
