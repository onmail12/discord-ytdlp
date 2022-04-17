def main():
    a = "**`dl help youtube`** to get youtube related helps\n\n**`dl help spotify`** to get spotify related helps\n\n**`dl help instagram`** to get instagram related helps\n\n**`dl help torrent`** to get torrent related helps\n\n**`dl help upscale`** to get upscale related helps"
    return a


def youtube():
    a = "**Youtube Help**\n`dl [(1080/720/480/360/240/144) / audio] [YT_URL]`"
    return a


def spotify():
    a = "**Spotify Help**\n`dl spot [TRACK/ALBUM/PLAYLIST_URL]`"
    return a


def ig():
    a = "**Instagram Help**\n`dl [INSTAGRAM VIDEO URL] [gd/dc/(empty)]`\n\ngd will returns google drive link\ndc will send instagram video to discord\n(empty) will returns streamable.com link"
    return a


def torrent():
    a = "**Torrent Help**\n`dl torrent [.TORRENT_URL]`"
    return a


def upscale():
    a = "**Upscale Help**\n`dl upscale [waifu2x/fsr] [IMG_URL]`"
    return a
