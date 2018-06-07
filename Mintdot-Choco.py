import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

token = 'NDUzNDM5NTQwMTg3ODg5Njg1.DfpM0w.dBIzKm-zBl--s8rPGRr2T6AeNU8'

bot = commands.Bot(command_prefix='-co ')

@bot.event
async def on_ready():
    print("CHOCO BOT IS READY")
    print("BOT NAME: " + bot.user.name)
    print("BOT ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="-co help"))

@bot.command(pass_context=True)
async def help(ctx):
    await bot.say('"-co co" 입력 시 오늘의 초코를 보실 수 있습니다.')

@bot.command(pass_context=True)
async def co(ctx):
    embed = discord.Embed(title="Let's co's time.")
    embed.set_author(name="1DAY 1CO", icon_url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    embed.set_image(url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    embed.set_footer(text="co is best dog", icon_url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    await bot.say(embed=embed)

bot.run(token)