import nextcord
from nextcord.ext import commands

bot = nextcord.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print("Discord Bot is now online!")
  
@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")
  
@bot.command()
async def hello(ctx):
  await ctx.send("Hello There!")
  
bot.run("token here")
