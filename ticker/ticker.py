import requests as r
import json

class Ticker(object):
    """Ticker docstring"""

    def __init__(self, key, source):
        self.key = key
        self.source = source

    def getNews(self):
        allNews = []
        newsInJSON = r.get("https://newsapi.org/v1/articles?source=" + self.source + "&sortBy=latest&apiKey=" + self.key).json()
        if newsInJSON['status'] == 'ok':
            for i in newsInJSON['articles']:
                allNews.append(i['title'])

            theNews = ""
            for i in allNews:
                theNews += "{} | ".format(i)

            return theNews
        else:
            return "not available"
    def parse(self, string):
        return string.replace('’', "'").replace('‘',"'").replace("…","...")


t = Ticker("a582288c6e954288a1ce26f79ad42123", "the-next-web")

news = t.parse(t.getNews())
print (news)
