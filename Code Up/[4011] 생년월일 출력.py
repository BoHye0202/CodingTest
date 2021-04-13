a,b = list(map(int, input().split('-')))
if b//1000000==1:
    s = 'M'
else:
    s='F'
y = a//10000
m = (a%10000)//100
print('19%02d/%02d/%02d %s' %(y,m,(a%10000)%100,s))