def solution(s, n):
    answer = list(s)
    l = []
    for i in answer:
        i = ord(i)
        if i==32:
            l.append(chr(i))
        else:
            if i<=90:
                i+=n
                if i>=91:
                    i=i-26
            elif i>=97:
                i+=n
                if i>=123:
                    i=i-26
            l.append(chr(i))
    return print(''.join(map(str,l)))

solution('AB',1)
solution('z',1)
solution('a B z', 4)