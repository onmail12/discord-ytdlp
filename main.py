import os


def getYtFileName(ytLink):
    cmd = 'python3 yt-dlp --get-filename -o "%(title)s.%(ext)s" -f b {}'.format(ytLink)
    return str(os.popen(cmd).read()).strip("\n")


def upload(fileName):
    cmd = './rclone copy "output\{}" GDrive:'.format(fileName)
    print("upload " + cmd)
    return str(os.popen(cmd).read())


def getDownloadLink(fileName):
    cmd = './rclone link GDrive:"output\{}"'.format(fileName)
    print("getDownloadLink ", cmd)
    return str(os.popen(cmd).read())


ytLink = input("Youtube: ")
cmd = 'python3 yt-dlp -o "output\%(title)s.%(ext)s" -f b {}'.format(ytLink)
print(cmd)
output = os.popen(cmd).read()
print("Done!")
upload(getYtFileName(ytLink))
print("Upload Done!")
print("Uploaded as " + getYtFileName(ytLink))
print("Download here " + getDownloadLink(getYtFileName(ytLink)))
try:
    os.remove(getYtFileName(ytLink))
except:
    print("The file does not exist")
