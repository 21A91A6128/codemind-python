_=int(input())
v=list(map(int,input().split()))
k=list(set(v))
r=[]
for i in k:
    if v.count(i)==1:
        r.append(i)
if len(r)==0:
    print(-1)
else:
    print(*r)