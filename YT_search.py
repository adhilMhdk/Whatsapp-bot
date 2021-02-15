from youtubesearchpython import VideosSearch


def search(Keyword):
    videosSearch = VideosSearch(Keyword, limit = 1)
    url = videosSearch.result().get("result")[0]['link']
    result = videosSearch.result().get("result")[0]['title']
    return result+" %0a "+url

