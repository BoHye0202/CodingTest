def solution(numbers, hand):

    return answer
# def solution(numbers, hand):
#     l = [1,4,7]
#     r = [3,6,9]
#     m = [2,5,8,0]
#     ln,rn = 0, 0
#     answer = []
#     for i in numbers:
#         if i in l:
#             ln=i
#             answer.append('L')
#         elif i in r:
#             rn=i
#             answer.append('R')
#         else:
#             a,b,c = ln//4,rn//4,i//4
#             k=min(abs(a-c),abs(b-c))
#             print(ln,rn,i,'check')
#             print(a,b,c)
#             if a==b:
#                 if hand=='right':
#                     rn = i
#                     answer.append('R')
#                 else:
#                     ln = i
#                     answer.append('L')
#             elif k == abs(a-c):
#                 ln = i
#                 answer.append('L')
#             elif k== abs(b-c):
#                 rn = i
#                 answer.append('R')
#     print(''.join(answer))
#     return ''.join(answer)

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right')
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left')
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right')