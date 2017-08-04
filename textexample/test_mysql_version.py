#-*- coding: utf-8 -*-
#安装 MYSQL DB for python
import MySQLdb as mdb
con = None
try:
  #连接 mysql 的方法： connect('ip','user','password','dbname')
  con = mdb.connect('localhost', 'root','root', 'test');
 
  #所有的查询，都在连接 con 的一个模块 cursor 上面运行的
  cur = con.cursor()
 
  #执行一个查询
  cur.execute("SELECT VERSION()")
  #取得上个查询的结果，是单个结果
 
  data = cur.fetchone()
  print "Database version : %s " % data
finally:
  if con:
    #无论如何，连接记得关闭
    con.close()
