vow=['a','e','i','o','u','A','E','I','O','U']
s=input()
v=[]
for i in s:
    if i in vow and i not in v:
        v.append(i)
if len(v)==0:
    print(-1)
else:
    for i in v:
        print(i,end=' ')