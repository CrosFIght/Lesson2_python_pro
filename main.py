import discord
from discord.ext import commands
from settings import settings
from bot_logic import gen_pass, Coin

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

#@bot.command()
#async def online(ctx):
    #online_members = sum(member.status == discord.Status.online for member in ctx.guild.members)
    #await ctx.send("Online: " + online_members)

bot.run(settings)
