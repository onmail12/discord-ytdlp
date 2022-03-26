from functions import *
import discord
import random

TOKEN = "OTU3MTQxNzMzNTc2MTc5NzUy.Yj6dtA.pobFo_Oi69lHNfBP9eYnCUxrX9M"
client = discord.Client()


@client.event
async def on_ready():
    print("BOT READY: {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("dl 1080 https://www.youtube.com/"):
        message.content = message.content.split()[1]
        print(message.content)
        await message.channel.send(mainGet(message.content))

    elif message.content.startswith("dl 720 https://www.youtube.com/"):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet720(message.content))

    elif message.content.startswith("dl 480 https://www.youtube.com/"):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet480(message.content))

    elif message.content.startswith("dl 360 https://www.youtube.com/"):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet360(message.content))

    elif message.content.startswith("dl 240 https://www.youtube.com/"):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet240(message.content))

    elif message.content.startswith("dl 144 https://www.youtube.com/"):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet144(message.content))


client.run(TOKEN)
