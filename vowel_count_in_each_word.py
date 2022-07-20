vow=['a','e','i','o','u']
for i in input().split(' '):
    a=0
    for j in i:
        if j in vow:
            a+=1
    print(a,end=' ')