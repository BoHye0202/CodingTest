from collections import deque
def solution2(prices): # O(n)
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer

def solution(prices): # O(n^2)
    answer = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i]>prices[j]:
                break
    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
print(solution([1, 1, 1, 1, 1])) # [4, 3, 2, 1, 0]
print(solution([1, 2, 3, 2, 3, 1])) # [5, 4, 1, 2, 1, 0]