import sys

sys.setrecursionlimit(10 ** 6)
from collections import deque

def bfs(n, k):
    used = [0] * 200001
    queue = deque()
    queue.append(n)
    used[n] = 1

    while queue:
        x = queue.popleft()
        for a in (x+1, x-1, 2*x):
            if 0<= a <= 200000 and used[a] == 0:
                queue.append(a)
                used[a] = used[x] + 1
        if x == k:
            return used[k] - 1


n, k = map(int, input().split())
print(bfs(n, k))
