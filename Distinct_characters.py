s=list(input().lower())
a=[]
for i in s:
    if i!=' ' and s.count(i)==1:
        a.append(i)
a.sort()
for i in a:
    print(i,end='')