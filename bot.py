"""Import Nextcord"""
import nextcord
from nextcord.ext import commands

bot = nextcord.Bot(command_prefix="!")

"""When the bot goes online, it will say it's online."""
@bot.event
async def on_ready():
  print("Discord Bot is now online!")

"""A ping command"""
@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")
  
"""A hello command"""
@bot.command()
async def hello(ctx):
  await ctx.send("Hello There!")

"""Will bring the bot online"""
bot.run("token here")
