vow=['a','e','i','o','u']
b=[]
for i in list(input()):
    if i in vow:
        b.append(i)
b=set(b)
if len(b)==5:
    print('0')
else:
    for i in vow:
        if i not in b:
            print(i,end=' ')