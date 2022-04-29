n=int(input())
for i in range(1,n+1,1):
    v=int(input())
    a=0
    for j in range(1,v,1):
        if j*j==v:
            a=a+1
    if a==0:
        print('False',end='
')
    else:
        print('True',end='
')