import os
import re
import random
from pystreamable import StreamableApi


def getRandom():
    return random.random()


def upload(fileName):
    cmd = 'rclone copy "{}" GDrive:'.format(fileName)
    print("upload " + cmd)
    return str(os.popen(cmd).read())


def getDownloadLink(fileName):
    cmd = 'rclone link GDrive:"{}"'.format(fileName)
    print("getDownloadLink ", cmd)
    return str(os.popen(cmd).read())


def removeLocal(fileName):
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")


def speedtest():
    print("testing speed...")
    cmd = "python speedtest-cli --simple"
    output = str(os.popen(cmd).read())
    print("speedtest done!")
    return output


def getYtId(ytLink):
    return re.search(
        "((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)", ytLink
    ).group()


def getYtFileName(ytLink):
    cmd = 'python yt-dlp --get-filename -o "%(title)s.%(ext)s" -f b {}'.format(
        getYtId(ytLink)
    )
    return str(os.popen(cmd).read()).strip("\n")


def mainGetBest(ytLink):
    cmd = 'python yt-dlp -o "%(title)s best.%(ext)s" -f b* {}'.format(getYtId(ytLink))
    cmd2 = 'python yt-dlp --get-filename -o "%(title)s best.%(ext)s" -f b* {}'.format(
        getYtId(ytLink)
    )
    print("-----getting best quality-----")
    print(cmd)
    output = os.popen(cmd).read()
    fileName = os.popen(cmd2).read().strip("\n")
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)


def mainGet720(ytLink):
    cmd = 'python yt-dlp -o "%(title)s 720.%(ext)s" -f b {}'.format(getYtId(ytLink))
    cmd2 = 'python yt-dlp --get-filename -o "%(title)s 720.%(ext)s" -f b* {}'.format(
        getYtId(ytLink)
    )
    print("-----getting 720 quality-----")
    print(cmd)
    output = os.popen(cmd).read()
    fileName = os.popen(cmd2).read().strip("\n")
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)


def mainGet144(ytLink):
    cmd = 'python yt-dlp -o "%(title)s 144.%(ext)s" -S "res:144" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python yt-dlp --get-filename -o "%(title)s 144.%(ext)s" -S "res:144" -f b {}'.format(
        getYtId(ytLink)
    )
    print("-----getting 144 quality-----")
    print(cmd)
    output = os.popen(cmd).read()
    fileName = os.popen(cmd2).read().strip("\n")
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)


def mainGet240(ytLink):
    cmd = 'python yt-dlp -o "%(title)s 240.%(ext)s" -S "res:240" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python yt-dlp --get-filename -o "%(title)s 240.%(ext)s" -S "res:240" -f b {}'.format(
        getYtId(ytLink)
    )
    print("-----getting 240 quality-----")
    print(cmd)
    output = os.popen(cmd).read()
    fileName = os.popen(cmd2).read().strip("\n")
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)


def mainGet360(ytLink):
    cmd = 'python yt-dlp -o "%(title)s 360.%(ext)s" -S "res:360" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python yt-dlp --get-filename -o "%(title)s 360.%(ext)s" -S "res:360" -f b {}'.format(
        getYtId(ytLink)
    )
    print("-----getting 360 quality-----")
    print(cmd)
    output = os.popen(cmd).read()
    fileName = os.popen(cmd2).read().strip("\n")
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)


def mainGet480(ytLink):
    cmd = 'python yt-dlp -o "%(title)s 480.%(ext)s" -S "res:480" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python yt-dlp --get-filename -o "%(title)s 480.%(ext)s" -S "res:480" -f b {}'.format(
        getYtId(ytLink)
    )
    print("-----getting 480 quality-----")
    print(cmd)
    output = os.popen(cmd).read()
    fileName = os.popen(cmd2).read().strip("\n")
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)


# ----------------------------- spot DL ----------------------------------- #


def getSpotFileName(cmdOutput):
    return cmdOutput.split('"')[1]


def mainSpot(spotLink):
    cmd = "spotdl {}".format(spotLink)
    print(cmd)
    output = os.popen(cmd).read()
    print("SPOTDL: " + output)
    fileName = getSpotFileName(output) + ".mp3"
    print("Downloading...")
    print("Downloaded as {}".format(fileName))
    print("Uploading {}".format(fileName))
    try:
        upload(fileName)
        print("Uploaded!")
    except:
        return "ERROR upload func"
    removeLocal(fileName)
    print("TASK DONE!")
    return getDownloadLink(fileName)


def playlistSpot(spotLink):
    # download
    print("cd playlist")
    os.chdir("playlist")
    cmd = "spotdl {}".format(spotLink)
    print(cmd)
    output = os.popen(cmd).read()
    print(output)

    # upload
    randomLocalValue = getRandom()
    os.chdir("../")
    os.system("rclone mkdir GDrive:playlist/{}".format(randomLocalValue))
    os.system("rclone copy playlist GDrive:playlist/{} -vP".format(randomLocalValue))
    cmdUpload = "rclone link GDrive:playlist/{}".format(randomLocalValue)
    print(cmdUpload)
    outputCmdUpload = os.popen(cmdUpload).read()
    print("deleting spot dl cache...")
    os.system("rclone delete GDrive:playlist/{}/.spotdl-cache".format(randomLocalValue))

    # deleting local file to save space...
    os.system("rm -r playlist/*")
    return outputCmdUpload


# ----------------------INSTAGRAM (YT-DLP)----------------


def vidInsta(instaLink):
    cmd = "yt-dlp {}".format(instaLink)
    output = str(os.popen(cmd).read())
    fileName = (
        output.split("[download]")[1]
        .replace(" has already been downloaded", "")
        .strip(" ")
        .strip("\n")
    )
    upload(fileName)
    return getDownloadLink(fileName)


def vidInstaDc(instaLink):
    cmd = "yt-dlp {}".format(instaLink)
    output = str(os.popen(cmd).read())
    fileName = (
        output.split("[download]")[1]
        .replace(" has already been downloaded", "")
        .strip(" ")
        .strip("\n")
        .strip("Destination: ")
    )
    removeLocal(fileName)
    print(fileName)
    return fileName


def vidInstaStream(instaLink):
    cmd = "yt-dlp {}".format(instaLink)
    output = os.popen(cmd).read()
    fileName = (
        output.split("[download]")[1]
        .replace(" has already been downloaded", "")
        .strip(" ")
        .strip("\n")
        .strip("Destination: ")
    )
    streamable = StreamableApi("protonu1122@tutanota.com", "Protonuonmail12.")
    cmdUpload = streamable.upload_video("{}".format(fileName))
    send = "https://streamable.com/" + cmdUpload["shortcode"]
    return send
