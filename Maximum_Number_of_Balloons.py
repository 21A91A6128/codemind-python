s=input()
txt=['a','b','l','o','n']
vk=''
for i in s:
    if i in txt:
        vk+=i
ans=[vk.count('a'),vk.count('b'),vk.count('l')//2,vk.count('o')//2,vk.count('n')]
print(min(ans))