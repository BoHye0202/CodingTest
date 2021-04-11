def solution(arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        x = [a+b for a,b in zip(i,j)]
        answer.append(x)
    print(answer)
    return answer

solution([[1,2],[2,3]],[[3,4],[5,6]])