_=int(input())
v=list(map(int,input().split()))
r=[]
for i in v:
    if i<0:
        i=abs(i)
    r.append(i)
r.sort()
for k in r:
    print(k*k,end=' ')