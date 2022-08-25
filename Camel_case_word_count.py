v=input()
r=0
for k in range(1,len(v)-1):
    if ord(v[k])>64 and ord(v[k])<91:
        r+=1
print(r+1)