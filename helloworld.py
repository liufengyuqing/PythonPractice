#coding=utf-8
'''
Created on 2017年5月11日

@author: lzw
'''
# !/usr/bin/python
print("Hello, World!")
print("hello")

if True:
    print("answer")
    print("TRUE")
else:
    print("Answer")
    print("false")

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

import sys

x = 'runoob'
sys.stdout.write(x + '\n')


def hello():
    return "hello world"

if __name__== "main":
    print hello()
