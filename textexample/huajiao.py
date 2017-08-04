# -*-coding:utf-8-*-
import urllib
from bs4 import BeautifulSoup
import re

def getliveids(url):
    html=urllib.urlopen(url)
    liveIds=set()
    bsobj=BeautifulSoup(html,'html.parser')
    for link in bsobj.find_all('a',href=re.compile('^(/l/)')):
        if 'href' in link.attrs:
            newpage=link.attrs['href']
            liveId=re.findall("[0-9]+",newpage)
            liveIds.add(liveId[0])
    return liveIds
#url ='http://www.huajiao.com/category/1000?pageno=1'

#print getliveids(url)
def getpage ():
    liveIds=set()
    liveIds=getliveids('http://www.huajiao.com/category/1000?pageno=1')|getliveids('http://www.huajiao.com/category/1000?pageno=2')
    return liveIds

def getUserId(liveId):
    html=urllib.urlopen('http://www.huajiao.com/'+'l/'+str(liveId))
    bsobj=BeautifulSoup(html,'html.parser')
    text=bsobj.title.get_text()
    res=re.findall('[0-9]+',text)
    return res[0]

#liveIds=getpage()
#for i in liveIds:
 #   print getUserId(i)

def getUserData(userid):
    print 'getUseerData:userId=',userid
    html=urllib.urlopen('http://www.huajiao.com/user/'+str(userid))
    bsobj=BeautifulSoup(html,'html.parser')
    data=dict()

    try:
        userInfoobj=bsobj.find('div',{'id':'userInfo'})
        data['Avatar']=userInfoobj.find('div',{'class':'avatar'}).img.attrs['src']
        data['UserId']=userid
        data['About']=userInfoobj.find('p',{'class':'about'}).get_text()
        tmp1=userInfoobj.h3.get_text('|',strip=1).split('|')
        data['UserName']=tmp1[0]
        data['Level']=tmp1[1]
        tmp2=userInfoobj.find('ul',{'class':'clearfix'}).get_text('|',strip=1).split('|')
        data['Follow']=tmp2[0]
        data['Fans']=tmp2[2]
        data['Compliments']=tmp2[4]
        data['Experience']=tmp2[6]
        return data
    except AttributeError:
        print str(userid)+U'出现错误'
        return None

def main():
    for liveId in getpage():
        userId=getUserId(liveId)
        userData=getUserData(userId)
        try:
            if userData:
                for userData_utf8 in userData:
                    userData_utf8.decode()
                print userData_utf8
        except Exception as e:
            print e

if __name__ == '__main__':
    main()



