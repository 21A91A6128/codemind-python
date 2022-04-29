v,k=map(int,input().split())
r=1
for r in range(k+1):
    if r%2!=0:
        print(v,'x',r,'=',v*r)