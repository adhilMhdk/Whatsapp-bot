from googlesearch import search

def getGoogleResult(keyword):
    for i in search(keyword, tld="com", num=1, stop=1):
        return i