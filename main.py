from functions import *
import discord
import random

TOKEN = "OTU3MTQxNzMzNTc2MTc5NzUy.Yj6dtA.ODpnYh8UrxdE7-Hp_sdjQfRxkRs"
client = discord.Client()


@client.event
async def on_ready():
    print("BOT READY: {0.user}".format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    authorId = "<@{}>".format(message.author.id)
    pajaId = "<@500626819880452097>"

    if message.content.startswith("dl 1080 "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGetBest(message.content))
        await message.add_reaction("✅")

    elif message.content.startswith("dl 720 "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGet720(message.content))
        await message.add_reaction("✅")

    elif message.content.startswith("dl 480 "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGet480(message.content))
        await message.add_reaction("✅")

    elif message.content.startswith("dl 360 "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGet360(message.content))
        await message.add_reaction("✅")

    elif message.content.startswith("dl 240 "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGet240(message.content))
        await message.add_reaction("✅")

    elif message.content.startswith("dl 144 "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGet144(message.content))
        await message.add_reaction("✅")
    # ---------------------------------------- INSTAGRAM (YT-DLP) --------------------------------------------------

    if message.content.startswith("dl https://www.instagram.com/"):
        print(message.content)
        instaLink = message.content.split()[1]
        try:
            uploadTo = message.content.split()[2]
        except:
            uploadTo = ""

        if uploadTo == "gd":
            await message.add_reaction("👍")
            await message.channel.send(vidInsta(instaLink))
            await message.add_reaction("✅")

        elif uploadTo == "dc":
            await message.add_reaction("👍")
            fileName = vidInstaDc(instaLink)
            try:
                await message.channel.send(file=discord.File("{}".format(fileName)))
                await message.add_reaction("✅")
            except:
                await message.channel.send(
                    authorId
                    + "\n"
                    + "File is bigger than 8 mb, beli nitro awkoakwoakowa"
                )
                await message.add_reaction("✅")

        elif uploadTo == "":
            await message.add_reaction("👍")
            instaLink = message.content.split()[1]
            await message.channel.send(authorId + "\n" + vidInstaStream(instaLink))
            await message.add_reaction("✅")

    # ---------------------------------------- SPOT-DL ----------------------------------------------------

    if message.content.startswith("dl spot https://open.spotify.com/"):
        message.content = message.content.split()[2]

        if message.content.startswith("https://open.spotify.com/playlist"):
            await message.add_reaction("👍")
            await message.channel.send(authorId + "\n" + playlistSpot(message.content))
            await message.add_reaction("✅")

        elif message.content.startswith("https://open.spotify.com/album"):
            await message.add_reaction("👍")
            await message.channel.send(authorId + "\n" + playlistSpot(message.content))
            await message.add_reaction("✅")

        elif message.content.startswith("https://open.spotify.com/track"):
            await message.add_reaction("👍")
            await message.channel.send(authorId + "\n" + mainSpot(message.content))
            await message.add_reaction("✅")

    # ---------------------------------------- MISC -----------------------------------------------------

    if message.content == "dl speedtest":
        await message.channel.send(authorId + "\n" + speedtest())

    if message.content == "dl help":
        await message.add_reaction("👍")
        await message.channel.send(
            authorId
            + "\n"
            + "**Download Youtube Video**\n`dl [RESOLUTION] [URL]` all args required\n\n**Download Spotify Track/Playlist/Album**\n`dl spot [TRACK/ALBUM/PLAYLIST URL]`\n\n**Download Instagram Video**\n`dl [INSTAGRAM VIDEO URL] [gd/dc/(empty)]` gd is google drive | dc is discord | leave empty is streamable (embed support)"
        )
        await message.add_reaction("✅")

    if message.content == "dl about":
        await message.channel.send(
            authorId
            + "\n"
            + "```Simple yt-dlp bot\nBot uploads all output files produced by yt-dlp to google drive using rclone\nHosted on heroku\n\nmade by Gouhund#3329```"
        )
    if message.content == "dl pingme":
        await message.channel.send(authorId)

    if message.content == "dl react":
        await message.add_reaction("👍")


client.run(TOKEN)
