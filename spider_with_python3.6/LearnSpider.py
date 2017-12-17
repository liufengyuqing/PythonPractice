import requests
from bs4 import BeautifulSoup
res = requests.get("http://news.sina.com.cn/gov/xlxw/2017-12-14/doc-ifypsqiz7398733.shtml")
res.encoding = "UTF-8"
context = res.text
#print(context)
soup = BeautifulSoup(context,'html.parser')
result = soup.select('.main-title')[0].text
print(result)
print(soup.select('#article_content')[0].text)