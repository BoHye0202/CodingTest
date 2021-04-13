a,b = map(int, input().split())
if b>a:
    a,b = b,a

def func(r, c, count, A) :
    # 0번째는 main에서 출력해주니 Index가 1인 경우부터 값을 구해준다.
    for i in range(1, count) :
        # 원하는 값이 1 이 아닌경우 리턴 해준다.
        if A[r-1][c-1] != 1 :
            return print(A[r-1][c-1] % 100000000)
        # 다음 행으로 넘어가기 전 숫자 구하는 부분 (이전 수 * 2)
        if i == count-1 :
            A[count-1][i] = A[count-1][i-1] * 2
            func(r, c, count+1, A)
        # 나머지 숫자 구하는 부분 ( 이전 수 + 바로 윗행의 수)
        else :
            A[count-1][i] = A[count-1][i-1] + A[count-2][i]

if a==1 or b==1:
    print(1)
else:
    A = [[1 for _ in range(a)] for _ in range(a)]
    func(a,b,2,A)

# def num(a,b):
#     if a==0:
#         l[0][b]=1
#         return 1
#     elif b==0:
#         l[a][0]=1
#         return 1
#
#     if l[a][b]==0:
#         l[a][b] = num(a-1,b)+num(a,b-1)
#     for i in l:
#         print(i)
#     return l
# print(num(a,b))