s=list(input().lower())
a=[]
for i in s:
    if i!=' ' and i not in a:
        a.append(i)
a.sort()
for i in a:
    print(i,end='')