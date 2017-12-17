print'hello'
print 'hello world'
mystring = 'python'
print mystring
print mystring[0:2]
print mystring[-1]
print mystring*2
print mystring+mystring
alist = [1,2,3,4]
print alist
print alist[0]
print alist[1:]
print alist[:3]
alist[1]=100
alist[0]='lzw'
print alist
yuanzu=(1,2,3,4)
print yuanzu
adict={'host':'earth'}
print adict
adict['host']=1000
print adict
print adict.keys()
adict['port'] = 999
print adict
for key in adict:
    print key,adict[key]

i=10
if i>1:
 print  'sb'


 for item in adict:
     print item,
for i in range(10):
    print i

se = [x**2 for x in range(100) if not x%2]
print se


