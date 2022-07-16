n=int(input())
a=list(map(int,input().split()))
b=set(a)
s,c=0,0
for i in b:
    if i==a.count(i):
        s+=i
        c+=1
if c==0:
    print('-1')
else:
 print("%.2f"%(s/c))