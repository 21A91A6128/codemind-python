a=b=0
for i in input().split(' '):
    a+=ord(min(i))
    b+=ord(max(i))
print(b-a)