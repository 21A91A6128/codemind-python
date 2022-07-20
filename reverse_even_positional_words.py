a=0
for i in input().split(' '):
    if a%2==0:
        i=i[::-1]
    a+=1
    print(i,end=' ')