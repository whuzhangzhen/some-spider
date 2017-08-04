#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

def loadIndex(url='http://jandan.net/ooxx'):#载入煎蛋网
    return urlopen(url).read()

def findPageTotal(html):#获取网站妹子图总页数
    pattern=re.compile(r'<span class="current-comment-page">\[(\d+)\]</span>')
    total=int(pattern.findall(html)[0])
    return total

def gethtml(page_id):#获取网站html
    res=requests.get('http://jiandan.net/ooxx/page-{}'.format(page_id))
    html=BeautifulSoup(res.text,"lxml")
    return html

#直接调用
Index=loadIndex()
total=findPageTotal(Index)
page_sum= int(input('how many pages:'))
for i in range(total):
    page_id = total - i
    if i==page_sum:
        break
    html=gethtml(page_id)
    for index ,each in enumerate(html.select('#comments img')):
        with open('{}-{}.jpg'.format(page_id,index),'wb') as jpg:
            #写入文件并格式化命名
           jpg.write(requests.get('http:'+each.attrs['src'],stream=True).content)




