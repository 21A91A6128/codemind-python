def prm(v):
    k=0
    for j in range(1,v+1,1):
        if v%j==0:
            k=k+1
    if k==2:
        return 1
    return 0
a,b,c,d=map(int,input().split())
for v in range(a,b+1):
    for k in range(c,d+1):
        if(prm(v+k)):
            break
        if(k==d):
            print('Takahashi')
            exit()
print('Aoki')