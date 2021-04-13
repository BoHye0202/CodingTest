n = int(input())
def check(n,a):
    num = n*a
    num = list(str(num))
    for x in num:
        if x!='1' and x!='0':
            return False
    return True
i = 1
while True:
    if i==100000000 or check(n,i)==True:
        print(n*i)
        break
    if check(n,i)==False:
        i+=1
        check(n,i)

