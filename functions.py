import os
import re


def getYtId(ytLink):
    return re.search(
        "((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)", ytLink
    ).group()


def getYtFileName(ytLink):
    cmd = 'python3 yt-dlp --get-filename -o "%(title)s.%(ext)s" -f b {}'.format(
        getYtId(ytLink)
    )
    return str(os.popen(cmd).read()).strip("\n")


def upload(fileName):
    cmd = './rclone copy "{}" GDrive:'.format(fileName)
    print("upload " + cmd)
    return str(os.popen(cmd).read())


def getDownloadLink(fileName):
    cmd = './rclone link GDrive:"{}"'.format(fileName)
    print("getDownloadLink ", cmd)
    return str(os.popen(cmd).read())


def mainGetBest(ytLink):
    cmd = 'python3 yt-dlp -o "%(title)s best.%(ext)s" -f b* {}'.format(getYtId(ytLink))
    cmd2 = 'python3 yt-dlp --get-filename -o "%(title)s best.%(ext)s" -f b* {}'.format(
        getYtId(ytLink)
    )
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
    cmd = 'python3 yt-dlp -o "%(title)s 720.%(ext)s" -f b {}'.format(getYtId(ytLink))
    cmd2 = 'python3 yt-dlp --get-filename -o "%(title)s 720.%(ext)s" -f b* {}'.format(
        getYtId(ytLink)
    )
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
    cmd = 'python3 yt-dlp -o "%(title)s 144.%(ext)s" -S "res:144" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python3 yt-dlp --get-filename -o "%(title)s 144.%(ext)s" -S "res:144" -f b {}'.format(
        getYtId(ytLink)
    )
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
    cmd = 'python3 yt-dlp -o "%(title)s 240.%(ext)s" -S "res:240" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python3 yt-dlp --get-filename -o "%(title)s 240.%(ext)s" -S "res:240" -f b {}'.format(
        getYtId(ytLink)
    )
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
    cmd = 'python3 yt-dlp -o "%(title)s 360.%(ext)s" -S "res:360" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python3 yt-dlp --get-filename -o "%(title)s 360.%(ext)s" -S "res:360" -f b {}'.format(
        getYtId(ytLink)
    )
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
    cmd = 'python3 yt-dlp -o "%(title)s 480.%(ext)s" -S "res:480" -f b {}'.format(
        getYtId(ytLink)
    )
    cmd2 = 'python3 yt-dlp --get-filename -o "%(title)s 480.%(ext)s" -S "res:480" -f b {}'.format(
        getYtId(ytLink)
    )
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
