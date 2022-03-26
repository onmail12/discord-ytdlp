import os


def getYtFileName(ytLink):
    cmd = 'python3 yt-dlp --get-filename -o "%(title)s.%(ext)s" -f b {}'.format(ytLink)
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
    cmd = 'python3 yt-dlp -o "%(title)s.%(ext)s [best]"-f b* {}'.format(ytLink)
    print(cmd)
    output = os.popen(cmd).read()
    fileName = getYtFileName(ytLink)
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
    cmd = 'python3 yt-dlp -o "%(title)s.%(ext)s [720]" -f b {}'.format(ytLink)
    print(cmd)
    output = os.popen(cmd).read()
    fileName = getYtFileName(ytLink)
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
    cmd = 'python3 yt-dlp -o "%(title)s.%(ext)s [144]" -S "res:144" -f b {}'.format(
        ytLink
    )
    print(cmd)
    output = os.popen(cmd).read()
    fileName = getYtFileName(ytLink)
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
    cmd = 'python3 yt-dlp -o "%(title)s.%(ext)s [240]" -S "res:240" -f b {}'.format(
        ytLink
    )
    print(cmd)
    output = os.popen(cmd).read()
    fileName = getYtFileName(ytLink)
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
    cmd = 'python3 yt-dlp -o "%(title)s.%(ext)s [360]" -S "res:360" -f b {}'.format(
        ytLink
    )
    print(cmd)
    output = os.popen(cmd).read()
    fileName = getYtFileName(ytLink)
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
    cmd = 'python3 yt-dlp -o "%(title)s.%(ext)s [480]" -S "res:480" -f b {}'.format(
        ytLink
    )
    print(cmd)
    output = os.popen(cmd).read()
    fileName = getYtFileName(ytLink)
    print("Downloaded!")
    upload(fileName)
    print("Uploaded as " + fileName)
    try:
        os.remove(fileName)
        print("File Removed!")
    except:
        print("File doesn't exist")
    return getDownloadLink(fileName)
