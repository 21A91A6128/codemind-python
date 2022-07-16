a=int(input())
b=list(map(int,input().split()))
c=b[::-1]
d,e,f,g=[],[],[],[]
for i in b:
    d.append(i)
for i in c:
    e.append(i)
for i in range(a):
    f.append(d[i])
    f.append(e[i])
for i in range(a):
    g.append(f[i])
if len(g)%2==0:
    print(*g)
else:
    g.append(0)
    print(*g)