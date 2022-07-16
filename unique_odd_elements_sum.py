_=int(input())
v=list(map(int,input().split()))
v=list(set(v))
c=0
for i in v:
    if i%2!=0:
        c+=i
print(c)