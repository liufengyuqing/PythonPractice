#coding=utf-8

import urllib
import re
import MySQLdb

class Sql(object):
    conn = MySQLdb.connect(host='localhost',user='root',passwd='1111',db='python',charset = 'utf-8')
    def addnovels(self,name):
        cur = self.conn.cursor()
        cur.exeute("")

def getSortList():
    res = urllib.urlopen('http://www.quanshuwang.com/map/1.html')
    html = res.read()
    html = html.decode('gbk')
    html = html.encode("utf-8")
    #print html
    reg = r'<a href="(/book/.*?)" target="_blank">(.*?)</a>'
    return re.findall(reg,html)
#getSortList()

def getChapterList(url):
    html = urllib.urlopen('http://www.quanshuwang.com%s'%url).read()
    html = html.decode('gbk')
    html = html.encode('utf-8')
    #print html
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    return re.findall(reg,html)

def getChapter(url,chapterUrl):
    #print 'http://www.quanshuwang.com%s' % url.split('/')[-1] + chapterUrl
    urls = url.split('/')[-1]
    print 'http://www.quanshuwang.com%s'%url.replace('index.html',chapterUrl)

    html = urllib.urlopen('http://www.quanshuwang.com%s'%url.replace('index.html',chapterUrl)).read()
    #html.decode('gbk').encode('utf-8')

    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    return re.findall(reg,html)

for novel in getSortList():
    #每本书的链接，书名
    #print i[0],i[1]
    url=novel[0]
    name = novel[1]
    print url, name
    #print getChapterList(url)
    #url = /book/0/151/index.html
    for chapter in getChapterList(url):
        #print chapter[0],chapter[1]
        chapterUrl = chapter[0]
        chapterName = chapter[1]
        print chapterUrl,chapterName
        print getChapter(url,chapterUrl)
        break
    break








