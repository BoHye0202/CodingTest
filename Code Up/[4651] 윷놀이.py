for i in range(3):
    l = list(map(int, input().split()))
    if l.count(1)==3:
        print('A')
    elif l.count(1)==2:
        print('B')
    elif l.count(1)==1:
        print('C')
    elif l.count(1)==0:
        print('D')
    else:
        print('E')