_=int(input())
v=list(map(int,input().split()))
for i in range(len(v)):
    k=0
    for j in range(len(v)):
        if v[i]>v[j]:
            k+=1
    print(k,end=' ')