from itertools import combinations
def solution(nums):
    answer = 0
    choice = len(nums)//2
    res = list(set(combinations(nums,2)))
    total = [sorted(i) for i in res]
    print(total)
    answer = list(combinations(total,choice))
    result = []
    print(answer)
    for i in answer:
        for j in i:
            print(j)
            if j[0] not in result:
                result.append(j[0])
            if j[1] not in result:
                result.append(j[1])

    print(result)
    return answer

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])