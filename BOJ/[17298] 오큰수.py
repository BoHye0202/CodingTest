n = int(input())
l = list(map(int, input().split()))
stack = []
res = [-1 for _ in range(n)]
# pop: stack에 element 존재, 가장 마지막이 비교대상보다 작으면 pop
# push: pop할 것들을 모두 pop해준 후에 비교대상이었던 값을 push



print(stack)
for i in range(n):
    print(res[i], end=' ')