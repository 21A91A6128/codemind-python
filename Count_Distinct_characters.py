s=list(input().lower())
a=[]
for i in s:
    if i!=' ' and i not in a:
        a.append(i)
print(len(a))