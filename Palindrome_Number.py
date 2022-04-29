n=int(input())
for i in range(1,n+1,1):
    v=int(input())
    t=v
    s=0
    while(v>0):
        r=v%10
        s=s*10+r
        v=v//10
    if t==s:
        print('True',end='
')
    else:
        print('False',end='
')