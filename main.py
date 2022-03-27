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

    if message.content.startswith("dl 1080 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGetBest(message.content))

    elif message.content.startswith("dl 720 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet720(message.content))

    elif message.content.startswith("dl 480 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet480(message.content))

    elif message.content.startswith("dl 360 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet360(message.content))

    elif message.content.startswith("dl 240 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet240(message.content))

    elif message.content.startswith("dl 144 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet144(message.content))

    elif message.content == "dl help":
        await message.channel.send("dl [resolution] [link]\n**all args required**")

    elif message.content == "dl speedtest":
        await message.channel.send(speedtest())


client.run(TOKEN)
