s=input()
a=len(s)
for i in s.split(' '):
    if(a>=len(i)):
        a=len(i)
print(a)