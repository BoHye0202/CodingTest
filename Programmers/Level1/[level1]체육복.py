def solution(n, l, r):
    now = n-len(l)
    k = list(set(l)&set(r))
    now+= len(k)
    l = [x for x in l if x not in k]
    r = [x for x in r if x not in k]
    for i in r:
        a,b = i-1,i+1
        if a in l:
            l.remove(a)
            now+=1
        elif b in l:
            l.remove(b)
            now+=1
    return print(now)

solution(5,[2, 4],[1, 3, 5])
solution(5,[2, 4],[3])
solution(3,[3],[1])
solution(5,[1,2,3],[2,3,4])#4
solution(8,[1,2,4,6],[1,2,4,6]) #8
solution(4,[3,1],[2,4]) #4