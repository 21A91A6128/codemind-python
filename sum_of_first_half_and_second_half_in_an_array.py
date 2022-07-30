a=int(input())
b=list(map(int,input().split()))
c=b[::-1]
d=e=0
for i in range(a//2):
    d+=b[i]
    e+=c[i]
if a%2!=0:
    e+=c[a//2]
print(d,e,sep='
')