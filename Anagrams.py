v=input().lower()
k=input().lower()
c=0
for i in v:
    for j in k:
        if i==j:
            c+=1
if c==len(k) and c==len(v):
    print(True)
else:
    print(False)