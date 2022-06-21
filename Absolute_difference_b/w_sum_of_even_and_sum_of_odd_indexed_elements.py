n=int(input())
v=list(map(int,input().split()))
a=b=0
for k in range(len(v)):
    if k%2==0:
        a+=v[k]
    else:
        b+=v[k]
print(abs(b-a))