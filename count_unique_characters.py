s=list(input().lower())
b=0
for i in s:
    if i!=' ' and s.count(i)==1:
        b+=1
print(b)