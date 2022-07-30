vow=['a','e','i','o','u','A','E','I','O','U ']
b=0
for i in input().split(' '):
    a=0
    i=list(i)
    for j in range(len(i)):
        if j==0 and i[j] in vow:
            a+=1
        if j==len(i)-1 and i[j] not in vow:
            a+=1
    if a==2:
        b+=1
print(b)