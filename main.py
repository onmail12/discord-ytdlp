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
    if message.content.startswith("dl https://www.youtube.com/"):
        message.content = message.content.strip("dl ")
        print(message.content)
        await message.channel.send(mainGet(message.content))


client.run(TOKEN)
