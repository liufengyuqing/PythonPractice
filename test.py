
print(abs(-100))
print(max(1,2,3,4))
print(int('12'))
print(float('12.2'))
print(str(1231))

def my_abs(x):
    if(x > 0):
        return x
    else:
        return -x

print(my_abs(-1))

L  = []
for x in range(1,11):
    L.append(x*x)

print(L )

L = [x * x for x in range(1,12)]

print(L)

import os

print([d for d in os.listdir(".")])

d = {"name":"liuzhiwei","age" : 23}

for k, v in d.items():
    print(k,'=',v)

L = [1]
while True:
    yield L
    L = [x+y for x,y in zip( [0]+L, L+[0] )]