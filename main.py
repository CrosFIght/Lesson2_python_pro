import discord
from settings import settings
from bot_logic import gen_pass, Coin

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hello'): 
        await message.channel.send("Hello, human being! How nice of you to contact me. What can I do for you today?")
    elif message.content.startswith('$Password'):
        await message.channel.send(f'Your password: \n||{gen_pass(10)}||')
    elif message.content.startswith('$Flip_coin'):
        await message.channel.send(f'Side of a coin: \n{Coin()}')
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    else:
        await message.channel.send(message.content)

client.run(settings)
