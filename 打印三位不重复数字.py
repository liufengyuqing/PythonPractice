#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python 练习题1--打印三位不重复数字
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

d = []
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a != b) and (a != c) and (c != b):
                # d.append([a,b,c])
                # d.append(str(a)+str(b)+str(c))
                d.append(100 * a + 10 * b + c)

print("总数量：", len(d))
print(d)

# 将for循环和if语句综合成一句，直接打印出结果
list_num = [1, 2, 3, 4]

list = [i * 100 + j * 10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]

print(list)

#参考方法(设置最大，最小值)：
line = []
for i in range(123, 433):
    a = i % 10
    b = (i % 100) // 10
    c = (i % 1000) // 100
    if a != b and b != c and a != c and 0 < a < 5 and 0 < b < 5 and 0 < c < 5:
        print(i,end=" ")
        line.append(i)

print()
print('the total is :', len(line))
