#coding=utf-8
__author__ = 'liuzhiwei'
''''
统计词频程序
'''
import  re #正则表达式模块
import sys  # 可以在任何用的时候引入，但是最好在最上面引入，比较清晰明了
import collections  # 容器模块

def is_chinese(uchar):
    '判断一个Unicode字符是否是中文'
    if uchar >= u'\u4E00'and  uchar <= u'\u9FA5':
        return True
    return False

def contain_chinese(ustr):
    '判断一个Unicode字符串是否是中文'
    for uchar in  ustr:
        if is_chinese(uchar):
            return True
        else:
            return False

def strip_symbols(ustr):
    '删除英文标点符号'
    return re.sub(u'[`!"#$%\'()*&+,-/:<=>^?@]',"",ustr)


def count_words(filename):
    '统计文件中非中文单词使用频率'

    words_count = collections.Counter() #实际上是一个dict ，但是他会帮我们自动的进行计数

    with open(filename,'rb') as fp: # 只读模式打开文件
        for line in fp:
            line = line.decode('utf-8').strip()
            if contain_chinese(line):
                continue

            line = strip_symbols(line)#删除英文标点符号
            line = line.lower() # 大写改小写
            words_count.update(re.split('\s+',line))

    return dict(words_count)


def get_top(filename,topk = 10):
    words_dict = count_words(filename)
    top_words = sorted(words_dict.items(),key=lambda p:p[1],reverse=True) #(word count)
    return top_words[:topk]#切片




if __name__ == '__main__':
    if len(sys.argv) !=3:
        print(sys.stderr,'useage:{} filename topk'.format(sys.argv[0]))
        sys.exit(1)

    topwords = get_top(sys.argv[1],int(sys.argv[2]))

    for word,count in topwords:
        print(word+" "+str(count))


