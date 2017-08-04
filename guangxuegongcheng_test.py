#-*- coding:utf-8 -*-

import urllib2
from  urllib import  urlopen
from bs4 import BeautifulSoup
from urllib2 import HTTPError
import re
import csv

def  gethtml(page_id):
    #获取光学期刊的html并返回
    page=urlopen('http://www.eope.net/CN/abstract/abstract{}.shtml'.format(page_id))
    html=page.read()
    return html


#for i in range(16854,16917):

    #try:

        #html=gethtml(page_id=i)
        #soup=BeautifulSoup(html,'html.parser')


        #spanlists=soup.find_all('span',class_='J_zhaiyao')
        #if spanlists:
         #  INFOList.append(spanlists[-1].get_text())
        #else:
         #   continue
    #except HTTPError:
        #print U'http error'
    #html = gethtml(page_id=i)
def getText(html):
    #获取作者摘要信息并返回
    soup = BeautifulSoup(html, 'html.parser')

    spanlists = soup.find_all('span', class_='J_zhaiyao')
    if spanlists:
       return  spanlists[-1].get_text()
    else:
        return None




def main():
    #调用gethtml（）和gettext（）
    INFOLists=[]
    for page_id in range(16854,16917):
        html=gethtml(page_id)
        INFOList=getText(html)
        INFOLists.append(INFOList)

    with open(info.csv,w) as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(INFOLists)

if __name__ == '__main__':
    main()







#for spanlist in spanlists:
    #print spanlist

#def getpage(page_id):

    #testpage=gethtml(url)
    #return testpage


#for i in range(16854,16917):

    #page_id=i
    #html=gethtml(page_id)
    #bsobj=BeautifulSoup(html,'html.parser')
    #print bsobj.span
    #print bsobj.prettify()
    #data=dict()
    #try:
        #anthur_infoobj=bsobj.find('span',{'class':'J_zhaiyao'})
        #data['name']=anthur_infoobj.strong.get_text()
        #data['name']=bsobj.find_all('span',{'class':'J_zhaiyao'}).strong
        #print  data['name']
    #except AttributeError:
        #print str(page_id)+U'出现错误'








