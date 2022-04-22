from functions import *
import helps
import discord
import random

TOKEN = "OTU3MTQxNzMzNTc2MTc5NzUy.Yj6dtA.ODpnYh8UrxdE7-Hp_sdjQfRxkRs"
client = discord.Client()


@client.event
async def on_ready():
    print("BOT READY: {0.user}".format(client))
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="dl help")
    )


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

    elif message.content.startswith("dl audio "):
        await message.add_reaction("👍")
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(authorId + "\n" + mainGetAudio(message.content))
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

    # ---------------------------------------- Tiktok (YT-DLP) --------------------------------------------------

    if message.content.startswith("dl https://www.tiktok.com"):
        await message.add_reaction("👍")
        instaLink = message.content.split()[1]
        await message.channel.send(authorId + "\n" + vidTTStream(instaLink))
        await message.add_reaction("✅")

    if message.content.startswith("dl yt-dlp"):
        await message.add_reaction("👍")
        instaLink = message.content.split()[2]
        await message.channel.send(authorId + "\n" + vidTTStream(instaLink))
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
    # ---------------------------------------- ARIA2C-TORRENT -----------------------------------------------------

    if message.content.startswith("dl torrent "):
        await message.add_reaction("👍")
        downloadLink = message.content.split()[2]
        await message.channel.send(authorId + "\n" + downloadTorrent(downloadLink))
        await message.add_reaction("✅")

    # ---------------------------------------- Upscaled -----------------------------------------------------

    if message.content.startswith("dl upscale fsr "):
        await message.add_reaction("👍")
        imgLink = message.content.split()[3]
        fileName = waifu2x(imgLink)
        try:
            await message.channel.send(file=discord.File("{}".format(fileName)))
            await message.add_reaction("✅")

        except:
            await message.channel.send(
                authorId + "\n" + "File is bigger than 8 mb, beli nitro awkoakwoakowa"
            )
            await message.add_reaction("✅")
        os.system("rm *.jpg")
        # await message.channel.send(superRes(imgLink))

    if message.content.startswith("dl upscale waifu2x "):
        await message.add_reaction("👍")
        imgLink = message.content.split()[3]
        # await message.channel.send(waifu2x(imgLink))
        fileName = waifu2x(imgLink)
        try:
            await message.channel.send(file=discord.File("{}".format(fileName)))
            await message.add_reaction("✅")

        except:
            await message.channel.send(
                authorId + "\n" + "File is bigger than 8 mb, beli nitro awkoakwoakowa"
            )
            await message.add_reaction("✅")
        os.system("rm *.jpg")

    # ---------------------------------------- MISC -----------------------------------------------------

    if message.content == "dl help":
        await message.channel.send(helps.main())

    if message.content == "dl help youtube":
        await message.channel.send(helps.youtube())

    if message.content == "dl help spotify":
        await message.channel.send(helps.spotify())

    if message.content == "dl help instagram":
        await message.channel.send(helps.ig())

    if message.content == "dl help torrent":
        await message.channel.send(helps.torrent())

    if message.content == "dl help upscale":
        await message.channel.send(helps.upscale())

    if message.content == "dl speedtest":
        await message.channel.send(authorId + "\n" + speedtest())

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

    if message.content == "dl test":
        await message.channel.send(testFunc())


client.run(TOKEN)
