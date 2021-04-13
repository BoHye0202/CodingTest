n = int(input())
if n<=500:
    res = n*0.7
elif n>500 and n<=1500:
    res = 350+(n-500)*0.4
elif n>1500 and n<=4500:
    res = 750+(n-1500)*0.15
elif n>4500 and n<=10000:
    res = 1200+(n-4500)*0.05
else:
    res = 1475+(n-10000)*0.02
print(int(res))