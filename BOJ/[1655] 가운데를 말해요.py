import heapq
import sys
input = sys.stdin.readline
left, right = [], []
n = int(input())
for i in range(n):
    x = int(input())
    if len(left)==len(right):
        heapq.heappush(right, (-x,x))
    else:
        heapq.heappush(left,(x,x))

    if left and right[0][1]>left[0][1]:
        t_max = heapq.heappop(right)[1]
        t_min = heapq.heappop(left)[1]
        heapq.heappush(right, (-t_min,t_min))
        heapq.heappush(left, (t_max, t_max))
    print(right[0][1])