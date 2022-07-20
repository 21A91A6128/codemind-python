vow=['a','e','i','o','u']
b=0
for i in input().split(' '):
    a=0
    for j in i:
        if j in vow:
            a+=1
    if(b<a):
        b=a
print(b)