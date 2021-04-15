# 메모리 초과 - 21.04.14
## 처음에 그냥 수열문제로만 푸니까 메모리 초과가 생겼다...
from itertools import combinations
n= int(input())
l = sorted(list(map(int, input().split())))
s = int(input())
p = list(combinations(l,2))
p = [sum(i) for i in p]
res = p.count(s)
print(res)

# 성공 - 21.04.15
n = int(input())
l = sorted(list(map(int, input().split())))
k = int(input())
a,b = 0,n-1
cnt = 0
while True:
    if a>=b:
        break
    if l[a]+l[b]==k:
        cnt+=1
        a +=1
    elif l[a]+l[b]<k:
        a+=1
    else:
        b-=1
print(cnt)

# 모범답안: 정렬, 투포인터 사용 문제
import sys
n= int(sys.stdin.readline())
l = sorted(list(map(int, sys.stdin.readline().split())))
s = int(sys.stdin.readline())

answer = 0
left, right = 0, n-1 # 왼, 오
while left<right:
    temp = l[left]+l[right]
    if temp == s:
        answer+=1
        left+=1
    elif temp<s:
        left+=1
    else:
        right-=1
print(answer)