import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
deq = deque([i for i in range(1, N + 1)])

ans = []
while deq:
    for _ in range(K-1):
        deq.append(deq.popleft())
    ans.append(deq.popleft())

print(str(ans).replace('[', '<').replace(']', '>'))
