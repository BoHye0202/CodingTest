res = 0
for i in range(5):
    s,e = map(float, input().split())
    if i==0:
        res+= 0 #(e-s)-1
    # elif i==0 and (e-s)<=1:
    #     res+=0
    else:
        res += (e-s)
total = (res)//0.5
print(total)
total-=4
if res>=15:
    total*=(0.95*5000)
elif res<=5:
    total*=(1.05*5000)
else:
    total*=5000
print(int(total))