#coding:utf-8
import requests
from lxml import html
from lxml import etree
#模拟浏览器的cookies登录的思路构造cookie
cookie={}

usr_cookie='SINAGLOBAL=3415039380273.1704.1474645755768; _s_tentry=www.liaoxuefeng.com; UOR=defcon.cn,widget.weibo.com,www.liaoxuefeng.com; Apache=5375637140938.245.1487169780442; ULV=1487169780455:4:3:2:5375637140938.245.1487169780442:1486988631658; login_sid_t=9e87e751abdefc437cb02f5c542aae2e; SUB=_2A251oBtGDeRxGeNN7FoS8S_PzDiIHXVW1AuOrDV8PUNbmtBeLWj5kW8jqvmIBwC2Xi1LdVHnpniGj-9Fjg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5rgk5aTag_iIHgOZS7LEK15JpX5KzhUgL.Fo-0S0n0eK20S0B2dJLoI0qLxKnLB-qLBoMLxK-L12qLB-zLxKqL1hnL1K2LxKqLBoMLBoMLxK-LB-BL1K5LxKMLB-zLBK5t; SUHB=0pHBEIjBMZxg5h; ALF=1518706324; SSOLoginState=1487170326; wvr=6'
#根据用户浏览器浏览的某个网站的cookies作为爬虫的初始cookies

for i in usr_cookie.split(';'):#将用户的cookies拆分成列表进行循环切割
    key,value=i.split('=',1)#将cookies中的每一个值进行拆分并存储到cookie{}中
    cookie[key]=value

page=requests.get('http://weibo.com/u/2969771025?refer_flag=1005050005_&is_all=1',cookies=cookie)
#利用cookies模拟浏览器抓取源网页的数据

#tree=html.fromstring(page.text)
#格式化page
selector=etree.HTML(page.__str__())
intro_raw=selector.xpath('//*[@id="Pl_Official_Headerv6__1"]/div/div/div[2]/div[3]/text()')

#简单的转码工作，这步根据需要可以省略
#for i in intro_raw:
 # intro = i.encode('utf-8')

print intro_raw



