import discord
from discord.ext import commands
from settings import settings
from bot_logic import *
import os
from images import *
from meme import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, human being! How nice of you to contact me. What can I do for you today?")

@bot.command()
async def password(ctx):
    await ctx.send(f'Your password: \n||{gen_pass(10)}||')

@bot.command()
async def coin_flip(ctx):
    await ctx.send(f'Side of a coin: \n{Coin()}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def image(ctx):
    images = os.listdir('images')
    print(images)
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('meme')
async def meme(ctx):
    with open("meme/meme.jpg", "r") as file:
        meme = file.read()
    await ctx.send(file=meme)

bot.run(settings)
