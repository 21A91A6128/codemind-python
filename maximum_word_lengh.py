s=input().split(' ')
a=len(min(s))
for i in s:
    if(a<=len(i)):
        a=len(i)
print(a)