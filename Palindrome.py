v=int(input())
t=v
s=0
while(v>0):
    r=v%10
    s=s*10+r
    v=v//10
if t==s:
    print('True')
else:
    print('False')