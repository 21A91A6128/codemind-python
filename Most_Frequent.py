_=int(input())
v=list(map(int,input().split()))
k=list(set(v))
k.sort()
l=0
res=k[-1]
for r in k:
    if v.count(r)>l:
        l=v.count(r)
        res=r
print(res)