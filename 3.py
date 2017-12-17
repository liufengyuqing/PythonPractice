#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 原答案没有指出三位数的数量，添加无重复三位数的数量

d=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (a!=c) and (c!=b):
                d.append([a,b,c])
print("总数量：", len(d))
print(d)