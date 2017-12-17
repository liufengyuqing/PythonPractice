# PythonPractice
学习Python的练习demo
python 还是很好玩的，刚开始在python2.7写的，后来用的python3.6
anaconda特别好用


python爬虫小例子

csdn博客 http://blog.csdn.net/qq_29232943/article/details/73824465

安装环境
pycharm 
python2.7
BeautifulSoup4

![这里写图片描述](http://oq7d8avf4.bkt.clouddn.com//17-6-27/28926171.jpg)

![这里写图片描述](http://oq7d8avf4.bkt.clouddn.com//17-6-27/39225695.jpg)

![这里写图片描述](http://oq7d8avf4.bkt.clouddn.com//17-6-27/91694638.jpg)


```
#coding=utf-8

import urllib
import urllib2
from bs4 import BeautifulSoup

url ='http://www.dbmeinv.com/?pager_offset=1'
x=1
def crawl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req =  urllib2.Request(url,headers=headers)#伪装浏览器访问
    page = urllib2.urlopen(req,timeout=20)#打开网页
    contents = page.read()#获取源码
    #print contents
    #html.parser解析网页xml功能更强大
    soup = BeautifulSoup(contents,'html.parser')#创建一个soup对象
    # 获取图片  find只找一次   find_all找到所有的标签    和正则表达式的区别
    my_girl = soup.find_all('img')
    print my_girl
    for girl in my_girl:
       # print girl
        link = girl.get('src')
        print link
        #下载图片，取名字
        global x
        urllib.urlretrieve(link,'E:\\image\%s.jpg'%x)
        print "正在下载%s。。。"% x
        x += 1  # 递增 python没有x++
        
for page in range(1,4):
    url = 'http://www.dbmeinv.com/?pager_offset=%s'%page
    crawl(url)
print "下载完毕。。。。"

crawl(url)

```


![这里写图片描述](http://oq7d8avf4.bkt.clouddn.com//17-6-27/95749375.jpg)
