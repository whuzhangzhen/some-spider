#-*-coding=utf-8-*-
import json
import urllib2 as httplib


# 正则表达式


class APIMgr:
    def __init__(self):
        self.apiLatest = 'http://news-at.zhihu.com/api/3/news/latest'
        self.apiBefore = 'http://news.at.zhihu.com/api/3/news/before/'
        self.apiID = 'http://news-at.zhihu.com/api/3/news/'

        # 知乎日报禁止了爬虫,因此要模拟浏览器访问
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}

    def access(self, url):
        self.req = httplib.Request(url, headers=self.headers)
        self.fp = httplib.urlopen(self.req)
        self.mybytes = self.fp.read()
        self.mystr = self.mybytes.decode("utf8")
        self.fp.close()
        return json.loads(self.mystr)

    def getLatestNews(self):
        return self.access(self.apiLatest)

    def getBeoreNews(self, date):
        return self.access(self.apiBefore + date)

    def getAssignedNews(self, id_):
        return self.access(self.apiID + id_)

    def parse(self):
        return json.loads(self.a)


class NewsMgr:
    def __init__(self, newsData):
        self.data = newsData

    def getType(self):
        return self.data['type']

    def getID(self):
        return self.data['id']

    def __repr__(self):
        return self.data


class SingleNews(NewsMgr):
    def __init__(self, apimgr, id_):
        NewsMgr.__init__(self, apimgr.getAssignedNews(id_))

    def getImages(self):
        return self.data['image']

    def getTitle(self):
        return self.data['title']

    def __len__(self):
        return len(self.getBody())

    def getImageSource(self):
        return self.data['date']

    def getGaOrefix(self):
        return self.data['ga_prefix']

    def getBody(self):
        return self.data['body']

    def getShareUrl(self):
        return self.data['share_url']

    def getCSS(self):
        return self.data['css'][0]


class AllDateNews(NewsMgr):
    def __init__(self, apimgr, date=''):
        if len(date) == 0:
            self.preData = apimgr.getLatestNews()
            NewsMgr.__init__(self, self.preData['stories'])
        elif self.dateIsLegal(date):
            self.preData = apimgr.getBeforeNews()
            NewsMgr.__init__(self, self.preData['stories'])
        else:
            raise 'DateError:date is not legal'

    def getImages(self):
        return self.data[0]['images'][0]

    def getNewsNum(self):
        return len(self.data)

    def getDate(self):
        return self.preData['date']

    def getStories(self):
        return self.data

    def __len__(self):
        return self.getNewsNum()

    def dateIsLegal(self, date):
        return re.match(r'(?!0000)[0-9]{4}[0-9]{4}', date)

    def getTitle(self, index):
        return self.data[index]['title']

    def getID(self, index):
        return self.data[index]['id']


if __name__ == '__main__':
    apimgr = APIMgr()
    print('-' * 100)
    print('知乎日报ID为4497219的文章题目是:')
    single = SingleNews(apimgr, '4497219')
    print('    ', single.getTitle())
    print('知乎日报ID为4497219的图片地址是:')
    print('    ', single.getImages())
    print('-' * 100)
    allnews = AllDateNews(apimgr)
    print('今日的知乎日报消息有:', len(allnews), '条')
    for index in range(len(allnews)):
        print('    标题:', allnews.getTitle(index), 'ID:', allnews.getID(index))