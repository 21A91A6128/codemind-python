vow=['a','e','i','o','u']
Vow=['A','E','I','O','U']
a=[]
b=[]
for i in input():
    if i in vow:
        a.append(i)
    elif i in Vow:
        b.append(i)
if(len(set(a))==5 or len(set(b))==5):
    print('True')
else:
    print('False')