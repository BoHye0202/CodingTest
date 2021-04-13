import sys
for line in sys.stdin:  # 입력이 끝날 때까지 입력을 받겠다
    # 누적합으로 k행 n열로 구해 볼 수 있을 것 같다.
    k, n = map(int, line.split())
    # 주의!! arr1 = [[-1]*(n+1)]*(k+1) 로 하면 모든 행 값이 같아지는 문제가 발생함...
    # 초기값은 우선 그냥 안나올 수인 (-1)로 선언해줌,
    # 총 크기가 k행n열이고 인덱스번호를 위치로 사용하고자 하여(n+1),(k+1).
    arr1 = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]

    def supersum(k, n):
        ## 1.정의 subersum(0,n) = n
        if k == 0:
            arr1[0][n] = n
            return n
        # 2. 초기값상태라면,계산하여 동작
        if arr1[k][n] == -1:
            result = 0
            for i in range(1, n + 1):  # 재귀 물레방아
                result += supersum(k - 1, i)  # 재귀
            arr1[k][n] = result  # 저장저장
            return result
        # 3. 이전에 동작하여 값이 있으면 재계산안하고 갖다 씀.
        else:
            return arr1[k][n]
    print(supersum(k, n))

# 20.12.03: 시간초과
def supersum(k, n):
    if k == 0:
        return n
    mysum = 0
    for i in range(1, n + 1):
        mysum += supersum(k - 1, i)
    return mysum

while True:
    k, n = map(int, input().split())
    if type(k)!=int:
        break

    print(supersum(k, n))