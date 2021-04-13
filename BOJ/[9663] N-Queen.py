def nqueen(sol,n): # sol: 정답배열 n
    global cnt

    if len(sol) == n: # sol이 n과 같아지면 cnt증가
        cnt +=1
        return 0
    candidate = [i for i in range(n)]
    for i in range(len(sol)):
        if sol[i] in candidate: #같은 열에 있는 지 확인
            candidate.remove(sol[i])
        distance = len(sol) - i
        if sol[i] + distance in candidate: #같은 대각선 상(+)에 있는지 확인
            candidate.remove(sol[i]+distance) # 같은 대각선 상에 있다면 후보에서 제외
        if sol[i] - distance in candidate: #같은 대각선 상(-)에 있는지 확인
            candidate.remove(sol[i]-distance)

        if candidate != []:
            for i in candidate:
                sol.append(i) # 후보의 요소를 정답 배열의 i+1로 추가
                nqueen(sol, n) # 재귀적으로 다음 행도 확인
        else:
            return 0

n = int(input())
cnt = 0
for i in range(n):
    nqueen([i], n)
print(cnt)