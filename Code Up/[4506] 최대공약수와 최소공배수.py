a,b = map(int, input().split())
mini, k=1,1
for i in range(2,min(a,b)+1):
    if a%i==0 and b%i==0:
        mini = max(mini,i)
print(mini)
print((a//mini)*(b//mini)*mini)