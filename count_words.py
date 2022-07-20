vow=['a','e','i','o','u','A','E','I','O','U']
a=0
for i in input().split(' '):
    s=list(i)
    if (s[0] in vow)and(s[-1] not in vow):
        a+=1
print(a)