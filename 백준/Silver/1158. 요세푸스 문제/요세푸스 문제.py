import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

numbers = list(x for x in range(1, n+1))
deq = deque(numbers)

ans = []

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    ans.append(deq.popleft())

print(str(ans).replace('[', '<').replace(']','>'))
