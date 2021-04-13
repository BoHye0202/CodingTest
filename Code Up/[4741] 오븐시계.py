a,b = map(int, input().split())
c = int(input())
x = c//60
y = c%60
min = (b+y)%60
hour = a+x+((b+y)//60)
if hour>23:
    hour-=24
print(hour, min)