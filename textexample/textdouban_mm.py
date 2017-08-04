
#-*-coding:utf-8-*- #编码声明，不要忘记！
import requests  #这里使用requests，小脚本用它最合适！
from lxml import html    #这里我们用lxml，也就是xpath的方法

#豆瓣模拟登录，最简单的是cookie，会这个方法，80%的登录网站可以搞定
cookie = {} 

raw_cookies = 'bid=ExZ9fp1uQAc; ll="118261"; dbcl2="137737001:c0MVlPVJtMk"; ck=6GB2; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1487167175%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dc2OpDJDbLM_HytTJO6WQ9C2n1zoPLazZNDgseIVAIWkz12Gbj5kuUhC4EdcM3Wi6%26wd%3D%26eqid%3Df948c90d00017bba00000005580f36f0%22%5D; __utmt=1; _vwo_uuid_v2=5099DCBCECAA3CD0BC6FEEA5A62D257E|45928827025b4043c4b054018ef75b3e; __utma=30149280.1458353226.1477392121.1486996010.1487167175.3; __utmb=30149280.4.10.1487167175; __utmc=30149280; __utmz=30149280.1477392121.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.13773; _pk_id.100001.8cb4=28638fa894fee82f.1477392120.3.1487167496.1486996038.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0'#引号里面是你的cookie，用之前讲的抓包工具来获得

for line in raw_cookies.split(';'):
    key,value = line.split("=", 1)
    cookie[key] = value #一些格式化操作，用来装载cookies

#重点来了！用requests，装载cookies，请求网站
page = requests.get('https://www.douban.com/people/146660450/',cookies=cookie)

#对获取到的page格式化操作，方便后面用XPath来
tree = html.fromstring(page.text)

#XPath解析，获得你要的文字段落！
intro_raw = tree.xpath('//span[@id="intro_display"]/text()')

#简单的转码工作，这步根据需要可以省略
for i in intro_raw:
    intro = i.encode('utf-8')

print intro #妹子的签名就显示在屏幕上
