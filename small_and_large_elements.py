s=input().split()
a=1
for i in s:
    if(a==1):
        print(min(i),end=' ')
    if(a==len(s)):
        print(max(i))
    a+=1