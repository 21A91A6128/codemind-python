s=list(input().lower())
for i in sorted(s):
    if i!=' ' and s.count(i)==1:
        print(i,end='')