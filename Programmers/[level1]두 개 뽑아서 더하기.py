from itertools import combinations, permutations
def solution(numbers):
    answer = list(combinations(numbers,2))
    answer = list(set(answer))
    new = []
    for i in answer:
        new.append(sum(i))
    new = list(set(new))
    return print(new)

solution([2,1,3,4,1])
solution([5,0,2,7])