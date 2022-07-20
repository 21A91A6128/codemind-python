vow=['a','e','i','o','u']
a=[]
b=[]
for i in input():
    if i in vow:
        a.append(i)
for i in vow:
    if i not in a:
        b.append(i)
if len(b)==0:
    print(0)
else:
    print(*(set(b)))