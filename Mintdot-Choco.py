import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

token = 'NDUzNDM5NTQwMTg3ODg5Njg1.DfpOCg.tkNCrOVrWvMP8Mrh9ejW8-QwojE'

bot = commands.Bot(command_prefix='-co ')

@bot.event
async def on_ready(self):
    print("CHOCO BOT IS READY")
    print("BOT NAME: " + bot.user.name)
    print("BOT ID: " + str(bot.user.id))
    await bot.change_presence(game=discord.Game(name="-co co"))

@bot.command(pass_context=True)
async def co(ctx):
    embed = discord.Embed(title="Let's co's time.")
    embed.set_author(name="1DAY 1CO", icon_url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    embed.set_image(url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    embed.set_footer(text="co is best dog", icon_url="https://raw.githubusercontent.com/Mintdot/Mintdot-Choco/master/img/co.png")
    await bot.say(embed=embed)

bot.run(token)