# -*- coding: UTF-8 -*-

def fib(num):
    a, b, L = 1, 1, []
    for n in range(num):
        L.append(a)
        #a, b = b, a + b
        c = a+b
        a = b
        b = c
    return L



if __name__ == "__main__":
    print fib(10)
