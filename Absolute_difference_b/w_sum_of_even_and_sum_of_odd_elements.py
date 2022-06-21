_=int(input())
v=list(map(int,input().split()))
a=b=0
for k in v:
    if k%2==0:
        a+=k
    else:
        b+=k
print(abs(a-b))