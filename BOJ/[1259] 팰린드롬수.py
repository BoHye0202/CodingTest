while True:
    l = list(map(int, input()))
    if l==[0]:
        break
    n = len(l)
    res = 'yes'
    for i in range((n//2)+1):
        if l[i]!=l[-(i+1)]:
            res = 'no'
            break
    print(res)

