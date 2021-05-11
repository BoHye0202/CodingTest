def solution(progresses, speeds):
    Q = []
    for i,j in zip(progresses, speeds):
        x = (100 - i) // j
        if (100-j)%j!=0:
            x+=1
        Q.append(x)
    result, i = [], 0
    cnt = 1
    print(Q)
    check = Q[i]
    while True:
        if i+1 == len(Q):
            result.append(cnt)
            break
        if check<Q[i+1]:
            result.append(cnt)
            cnt = 1
            check = Q[i+1]
        else:
            cnt+=1
        i+=1
    print(result)
    return result
# def solution(progresses, speeds):
#     Q = []
#     for i,j in zip(progresses, speeds):
#         x = (100-i)//j
#         Q.append(x)
#     result, i = [], 0
#     cnt = 1
#     while sum(result) != len(Q):
#         if i+1 == len(Q):
#             result.append(cnt)
#             cnt = 1
#             break
#         elif Q[i]<Q[i+1]:
#             result.append(cnt)
#             cnt = 1
#         elif Q[i]>=Q[i+1]:
#             cnt+=1
#         i+=1
#     print(result)
#     return result

solution([93, 30, 55], 	[1, 30, 5]) # [2, 1]
solution([95, 90, 99, 99, 80, 99], 	[1, 1, 1, 1, 1, 1]) # [1, 3, 2]
solution([98, 99, 97, 96], [1, 1, 1, 1]) # [2,1,1]
solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5, 10, 7]) #[1,2,3]
solution([93, 30, 55, 60, 40, 65],  [1, 30, 5 , 10, 60, 7]) # [2,4]