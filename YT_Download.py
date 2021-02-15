import pytube


def downloadVideo(url):
    youtube = pytube.YouTube(url)
    print(youtube)
    # or
    video = youtube.streams.get_lowest_resolution()
    print(video)
    # or
    path = '/home/adhil/PycharmProjects/WhatsappBot/downloads/'
    video.download(path)  # In
    return path + video.title + ".mp4"