n=int(input())
v=list(map(int,input().split()))
for i in range(0,n,2):
    for _ in range(v[i+1]):
        print(v[i],end=' ')