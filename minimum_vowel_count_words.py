s=input().split(' ')
vow=['a','e','i','o','u','A','E','I','O','U']
b=[]
d=0
for i in s:
    a=0
    for j in i:
        if j in vow:
            a+=1
    b.append(a)
c=min(b)
for i in s:
    a=0
    for j in i:
        if j in vow:
            a+=1
    if c==a:
        d+=1
print(d)