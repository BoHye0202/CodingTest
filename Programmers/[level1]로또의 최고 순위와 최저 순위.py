def solution(lottos, win_nums):
    x = {6:1,5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    union = list(set(lottos)&set(win_nums))
    num = lottos.count(0)
    return [x[len(union)+num], x[len(union)]]