import urllib
import webbrowser
url="http://www.baidu.com"
content=urllib.urlopen(url).read()
#print content;
open('python.html','w').write(content)
webbrowser.open_new_tab('python.html')
