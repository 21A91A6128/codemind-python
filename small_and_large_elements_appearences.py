s=list(input())
for i in s:
    if i==' ':
        s.remove(i)
print(min(s),s.count(min(s)),max(s),s.count(max(s)))