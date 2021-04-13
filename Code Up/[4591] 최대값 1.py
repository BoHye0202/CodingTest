l = []
for i in range(9):
    l.append(int(input()))
new = sorted(l)
print(new[-1])
print(l.index(new[-1])+1)