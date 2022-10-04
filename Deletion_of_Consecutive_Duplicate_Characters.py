for _ in range(int(input())):
    s=list(input())
    vk=0
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            vk+=1
    print(vk)