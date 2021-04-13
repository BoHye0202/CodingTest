#20.12.02: 실패
n = int(input())
l = list(map(int, input().split()))
l.sort()
mini = 1e9
for i in range(len(l)//2+1):
    print(l[i],l[-1-i])
    if l[i]+l[-1-i]<0:
        mini = max(-mini,l[i]+l[-1-i])
    elif l[i]+l[-1-i]==0:
        mini = l[i]+l[-1-i]
    else:
        mini = min(mini, l[i]+l[-1-i])

    if mini == l[i]+l[-1-i]:
        a=l[i]
        b=l[-1-i]

print(a,b)

# 모범코드
import sys
input = sys.stdin.readline

N = int(input())
liquid = [int(x) for x in input().split()]
liquid.sort()
left = 0 #왼쪽에서 시작하는 인데스
right = N - 1 #오른쪽에서 시작하는 인덱스
answer = liquid[left] + liquid[right] # 양과 음의 합이 되기 위해 양끝더하기
al = left #인덱스 저장
ar = right #인덱스 저장
while left < right: #인덱스가 엇갈릴때까지 반복
    tmp = liquid[left] + liquid[right] #더한 값이
    if abs(tmp) < abs(answer): #더한 값이 처음에 더한 저장값보다 작으면
        answer = tmp # 정답값이 바뀌고
        al = left # 인덱스도 따로 다시 저장해주고
        ar = right
        if answer == 0: # 심지어 합이 0이면 더 작은 수는 나올수없기 떄문에
            break # while문 나가기
    if tmp < 0: #만약에 tmp합이 음수였다면
        left += 1 # 왼쪽 인덱스를 1증가시키고
    else: # 그게 아니면
        right -= 1 #오른쪽 인덱스를 1감소시키기
print(liquid[al], liquid[ar])