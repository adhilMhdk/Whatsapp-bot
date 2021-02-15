import wikipedia
def getResult(question):
    try:
        ans = str(wikipedia.summary(question))
        return ans
    except:
        ans = str(wikipedia.search(question))
        return ans
