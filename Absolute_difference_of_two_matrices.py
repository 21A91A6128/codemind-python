n=int(input())
v=[]
for _ in range(n):
    v.append(list(map(int,input().split())))
k=[]
for _ in range(n):
    k.append(list(map(int,input().split())))
r=[[abs(v[i][j]-k[i][j]) for j in range(n)]for i in range(n)]
for i in r:
    print(*i)