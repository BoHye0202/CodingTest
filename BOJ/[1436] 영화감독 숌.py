n = int(input())
s = '666'
k = 666
ch = 0
while True:
    if ch == n:
        print(k-1)
        break

    if s in str(k):
        ch+=1
    k += 1
