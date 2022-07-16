_=int(input())
l=list(map(int,input().split()))
v,k=map(int,input().split())
c=[]
for i in l:
    if i>=v and i<=k:
        c.append(i)
if c==[]:
    print('-1')
else:
    print(*c)