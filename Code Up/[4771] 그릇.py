s = list(input())
res = 10
for i in range(1,len(s)):
    if s[i]==')' and s[i-1]=='(':
        res+=10
    elif s[i]=='(' and s[i-1]==')':
        res+=10
    elif s[i]=='(' and s[i-1]=='(':
        res+=5
    else:
        res+=5
print(res)
