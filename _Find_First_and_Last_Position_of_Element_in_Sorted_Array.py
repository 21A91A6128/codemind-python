_=int(input())
v=list(map(int,input().split()))
k=int(input())
a=b=-1
for i in range(len(v)):
    if k!=v[i]:
        continue
    if a==-1:
        a=i
    b=i
print(a,b)