def solution(arr):
    answer = [arr[0]]
    k = arr[0]
    for i in arr[1:]:
        if k!=i:
            answer.append(i)
        k=i

    return print(answer)

solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])