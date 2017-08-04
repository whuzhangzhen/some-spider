#coding:utf-8
from urllib2 import Request,urlopen
from urllib2  import HTTPError,URLError
import re,time
import requests
from bs4 import BeautifulSoup


def loadIndex(url='http://jandan.net/ooxx'):#载入html
    return urlopen(url).read()

def findPageTotal(html):#返回图片总页数
    pattern=re.compile(r'<span class="current-comment-page">\[(\d+)\]</span>')
    total=int(pattern.findall(html)[0])
    return total

def loadPage(page_id):#载入具体图片页面
    page_url='http://jandan.net/ooxx/page-{}'.format(page_id)
    try:
        page=urlopen(page_url).read()
    except (HTTPError,URLError) as e:
        return False
    return page

def findImages(html):#匹配页面对应的妹子图片
    #pattern=re.compile(r'<img src="([a-zA-z]*：*//[^\s]*.jpg)"')
    #image_urls=set(pattern.findall(html))
    html=BeautifulSoup(html,'lxml')
    image_urls=html.select('#comments img')
    return image_urls

def downloadImage(image_url,filename):#下载妹子图片


    try:
        req=Request(image_url,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')
        image_data=urlopen(req).read()
    except (HTTPError,URLError) as e:
        time.sleep(0.1)
        continue
    open(filename,'wb').write(image_data)
    break

def main(count=1):
    index=loadIndex()
    total=findPageTotal(index)
    for i in range(total):
        page_id=total-i
        print ('Now download images from page{}'.format(page_id))
        page=loadPage(page_id)
        if not page:continue
        image_urls_raw=findImages(page)
        pattern = re.compile(r'^//(.+).jpg')
        image_urls=re.findall(pattern,str(image_urls_raw))

        #print image_urls_raw[0]
        #image_urls=[]
        #for i in range(len(image_urls_raw)):
            #pattern = re.compile(r'<img src="(.*)"/>')
            #print re.findall(pattern,str(image_urls_raw[i]))
            #image_urls_li=str(re.findall(pattern,str(image_urls_raw[i])))
            #print image_urls_li.strip('')
            #image_urls.append(image_urls_li)
        #print image_urls
        image_id=0
        for image_url in image_urls:
            downloadImage(image_url,'{}-{}'.format(page_id,image_id))
            image_id+=1

if __name__=='__main__':
    count=int(input('how many pages:'))
    main(count)

