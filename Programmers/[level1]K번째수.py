def solution(array, commands):
    answer = []
    for i in commands:
        prom = array[i[0]-1:i[1]]
        prom = sorted(prom)
        answer.append(prom[i[-1]-1])
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])