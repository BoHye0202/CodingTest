def solution(arr, divisor):
    answer = []
    for i in arr:
        if i%divisor==0:
            answer.append(i)
    if len(answer)==0:
        return -1
    else:
        return print(answer)

solution([5, 9, 7, 10],5)
solution([2, 36, 1, 3],1)
solution([3,2,6],10)