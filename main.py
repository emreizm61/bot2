import discord
from discord.ext import commands
from bot_mantik import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has joined!')

@bot.command()
async def rock(ctx):
    await ctx.send(sanatci())
@bot.command()
async def akustik(ctx):
    await ctx.send(acoustic())
@bot.command()
async def rap(ctx):
    await ctx.send(rapci())    
@bot.command()
async def rockgif(ctx):
    await ctx.send(sanatcigif())
@bot.command()
async def akustikgif(ctx):
    await ctx.send(acousticgif())
@bot.command()
async def rapgif(ctx):
    await ctx.send(rapcigif())

bot.run('AL SANA TOKEN HEHEHEHE')