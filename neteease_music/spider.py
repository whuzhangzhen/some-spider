#-*-coding:utf-8-*-
import urllib2
from urllib import urlopen
from bs4 import BeautifulSoup
import requests


def getHtml(url):
    #获取歌词页面
    page=requests.get(url).content
    return page


url='http://music.163.com/#/song?id=202373'
page=getHtml(url)
soup=BeautifulSoup(page,'lxml')
lyric=soup.find_all('div',attrs={'data-song-id':'467952330'})

print lyric









