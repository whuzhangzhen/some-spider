#-*-coding:utf-8-*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
 
text_from_file_with_apath = open('/home/zz/Desktop/PycharmProjects/kechengsheji/tag_info.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
 
