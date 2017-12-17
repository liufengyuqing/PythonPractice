#coding=utf-8
import urllib,re,time,socket,urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#ascii输出的内容是utf-8格式

fanli_url = "http://zhide.fanli.com/p1"#主页
format_url = "http://zhide.fanli.com/detail/1-750345?spm=zhide_detail.pc.id-750345~cid-17"

#获取源码
class Fanly():
    def __init__(self):#必须拥有self 参数，本身
     self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
     self.html_data = []#放置商品
    #获取多页主页源码
    def get_html(self,start_page = 1,end_page=3):
        for i in range(start_page,end_page+1):
            rt= urllib2.Request('http://zhide.fanli.com/p%s'%i)#创建一个request
            #rt= urllib2.Request('http://zhide.fanli.com/p'+str(i))#创建一个request

            rt.add_header('User_Agent',self.user_agent)
            try:
                my_data = urllib2.urlopen(rt).read()
                #print my_data
                self.html_data.append(my_data)
                time.sleep(0.5)
                socket.setdefaulttimeout(5)
            except urllib2.URLError,e:
                if hasattr(e,'reason'):
                    print u"链接失败"
        return str(self.html_data)


#html = Fanly().get_html()
class GetData():
    def __init__(self):
        self.html = Fanly().get_html() #调用获取主页源码
        self.href =[]
        self.ls = []
        self.url= []

        #获取商品超链接
    def get_hrefurl(self):
        reg = r'data-id="\d{6}"'
        result = re.compile(reg)#编译，提高效率
        tag = result.findall(self.html)
        #tag = re.findall(result,self.html)
        #print tag
        for i in tag:
            self.href.append(i)
            #print self.href

        #去掉重复的，完整的连接诶
        reg2 = r"\d{6}"
        result2 = re.findall(reg2,str(self.href))
        if len(result2):
             for data in result2:
                if data not in self.ls:
                    self.ls.append(data)
                    url = 'http://zhide.fanli.com/detail/1-'+str(data)
                    self.url.append(url)
                    #print self.url
        return self.url

a = GetData().get_hrefurl()


class Href_mg():
    def __init__(self):
        self.list = GetData().get_hrefurl()
        self.txt_list = []

    def show_mg(self):
        for item in range(len(self.list)):
            if len(self.list):
                url = str(self.list[item])
                mg = urllib2.Request(url)
                try:
                   req = urllib2.urlopen(mg).read()
                   soup = BeautifulSoup(req,"html.parser")
                   txt = soup.find_all('h1')
                   self.txt_list.append(txt)
                   #print self.txt_list
                except urllib2.URLError,e:
                    print e.reason
        return str(self.txt_list).decode("unicode_escape")#反编码

#data = Href_mg().show_mg()

#写入文件
if __name__ =="__main__":
    path = "a.txt"
    with open(path,'a') as file:
        data = Href_mg().show_mg()
        reg4 = r'<.+?>'
        data_s = re.sub(reg4,' ',data).replace('全网最低','').replace('[','').replace(']','').replace(',','\n').strip().replace(' ','')
        print data_s
        file.write(data_s)




