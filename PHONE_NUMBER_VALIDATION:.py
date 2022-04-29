n=int(input())
a=0
while(n):
    a+=1
    n=n/10
    if(a==335 and n==0):
        a=a-1
if(a==334):
    print('Valid')
else:
    print('Invalid')