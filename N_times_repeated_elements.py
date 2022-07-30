_=int(input())
a=list(map(int,input().split()))
n=int(input())
b=[]
for i in a:
    if n==a.count(i) and i not in b:
        b.append(i)
if len(b)==0:
    print(-1)
else:
    print(*b)