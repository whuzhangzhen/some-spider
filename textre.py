import re 
m=re.findall("abc","aaaaabccccabcc")
print m

n=re.findall(r"<div>(.*)</div>","<div>hello,world!</div>")
print n
