import requests
from bs4 import BeautifulSoup
import time

def  crawl_joke_list_usebs4(page=1):
    url="http://www.qiushibaike.com/8hr/page/"+str(page)
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"lxml")
    joke_list = soup.find_all("div", class_="article block untagged mb15")
    print joke_list

if __name__=='main':
    crawl_joke_list_usebs4(1)

