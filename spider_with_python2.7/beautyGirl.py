#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import re
# 初始url
first_url = "http://www.xiaohuar.com/hua/"
# 发送一个请求
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# 包装一个请求
req = urllib2.Request(url=first_url, headers=header)

response = urllib2.urlopen(req)
# 获取返回的html
html = response.read()
# 我们要提取所有我们需要的img
soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
# 获取所有的img
imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+/\w+\.jpg'))

for img in imgs:
    # 创建一个请求
    # "/d/file/20170707/f7ca636f73937e33836e765b7261f036.jpg"
    url = "http://www.xiaohuar.com%s" % img['src']
    req = urllib2.Request(url=url, headers=header)
    # 获得了我们的图片信息
    data = urllib2.urlopen(req).read()
    # 保存图片
    with open('%s.jpg' % img['alt'], 'wb') as f:
        f.write(data)