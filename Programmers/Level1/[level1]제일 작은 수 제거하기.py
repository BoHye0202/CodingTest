def solution(arr):
    if len(arr)==1:
        return [-1]
    else:
        print(arr)
        arr.remove(min(arr))
        print(min(arr), arr)
        return arr

solution([4,3,2,1])
solution([10])