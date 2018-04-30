# print absolute value of an integer

while(True):
    num = input("please input an integer:")
    num_int = int(num)
    if num_int >= 0:
        print(num_int)
    else:
        print(-num_int)


for i in range(1,101):
    if i % 7 == 0:
        print(i)
#索引迭代
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print (index, '-', name)

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L)+1), L):
    print(index, '-', name)
#迭代dict的value
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print (d.values())
# [85, 95, 59]
for v in d.values():
    print (v)

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for v in d.itervalues():
    sum = sum + v
print (sum / len(d))

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
print (d.items())
for key, value in d.items():
    print (key, ':', value)

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print (k, ':', v)
print ('average', ':', sum / len(d))

