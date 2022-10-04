s=list(input())
vk=a=0
for i in range(0,len(s)-1):
    if(s[i]==s[i+1]):
        a+=1
    else:
        a=0
    if(vk<a):
        vk=a
print(vk+1)