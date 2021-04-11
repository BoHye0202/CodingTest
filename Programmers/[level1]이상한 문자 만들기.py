def solution(s):
    l = s.split(' ',-1)
    result = []
    for i in l:
        answer = []
        for j in range(len(i)):
            if j%2==0:
                answer.append(i[j].upper())
            else:
                answer.append(i[j].lower())
        result.append(''.join(map(str, answer)))
    return print(' '.join(map(str, result)))

solution(" try hello world ")
solution("HI BOHYE")
solution("Hello eVeryone") # "HeLlO EvErYoNe"
solution("sp ace") # "Sp AcE"
solution("AAAAAAAAAAA A A A A AAAAA AAA ") # "AaAaAaAaAaA A A A A AaAaA AaA "
