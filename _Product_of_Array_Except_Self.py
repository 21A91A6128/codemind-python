_=int(input())
v=list(map(int,input().split()))
for i in v:
    r=1
    for k in range(len(v)):
        if v[k]!=i:
            r*=v[k]
    print(r,end=' ')