n = input()
x = int(str(n)[::-1])
print(x)
l = [int(i) for i in str(x)]
print(sum(l))