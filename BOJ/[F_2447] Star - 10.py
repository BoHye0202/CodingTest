# 모범코드
def star(n):
    l =[]
    for i in range(3*len(n)):
        if i//len(n)==1: # if문은 중간줄에 빈칸만들려고 if문으로
            l.append(n[i%len(n)]+' '*len(n)+n[i%len(n)]) #append는 각 3개의 모양을 3배씩 늘리면서 아래로 줄늘리게 해주려고
        else:
            l.append(n[i%len(n)]*3)
    return list(l)

new = ['***','* *','***']
n = int(input())
k = 0
while n!=3:
    n = int(n/3)
    k+=1

for i in range(k):
    new = star(new)
for i in new:
    print(i)