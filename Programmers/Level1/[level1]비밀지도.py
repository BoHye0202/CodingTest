def solution(n, arr1, arr2): #비트연산자를 쓰면 더 짧아질 수 있다
    a,b = [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        num1, num2 = format(arr1[i],'b'), format(arr2[i],'b')
        l1, l2 = list(map(int, str(num1))), list(map(int, str(num2)))
        a[i][n-len(l1):] = l1
        b[i][n-len(l2):] = l2

    answer = []
    for i in range(n):
        k = ['#' if a[i][j]==1 or b[i][j]==1 else " " for j in range(n)]
        answer.append(''.join(map(str, k)))
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])