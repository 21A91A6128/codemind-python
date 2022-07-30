n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
b=0
for i in a:
    if i<x or i>y:
        b+=i
print(b)