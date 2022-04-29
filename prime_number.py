v=int(input())
k=0
for j in range(1,v+1,1):
    if v%j==0:
        k=k+1
if k==2:
    print('prime')
else:
    print('not a prime')