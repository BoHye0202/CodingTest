def solution(arr1, arr2):
    answer = []
    arr2 = list(map(list, zip(*arr2)))
    for i in arr1:
        result = []
        for j in arr2:
            x =[a*b for a,b in zip(i,j)]
            result.append(sum(x))
        answer.append(result)
    return answer

print(solution(	[[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]