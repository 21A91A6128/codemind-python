a=list(input().lower())
b=list(input().lower())
c=0
if len(a)==len(b):
    for i in a:
        if i in b:
            c+=1
    if c==len(a):
        print('True')
    else:
        print('False')
else:
    print('False')