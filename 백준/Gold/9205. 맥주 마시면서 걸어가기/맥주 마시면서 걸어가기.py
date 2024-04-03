import sys
from collections import deque
input = sys.stdin.readline


def bfs(r, c):
    queue = deque()
    visited[0] = 1
    queue.append((r,c))

    while queue:
        x, y = queue.popleft()
        for q in range(1, len(arr)+1):
            nr, nc = arr[q-1]
            if (abs((x-nr)) + abs((y-nc)))/50 <= 20 and visited[q] == 0:
                visited[q] = 1
                queue.append((nr, nc))


T = int(input())
for tc in range(T):
    n = int(input())
    arr = []
    sx, sy, ex, ey = 0, 0, 0, 0
    for i in range(n+2):
        if i == 0:
            sx, sy = map(int, input().split())
        else:
            a, b = map(int, input().split())
            arr.append((a, b))
    visited = [0] * (n+2)
    bfs(sx, sy)
    if visited[len(arr)]:
        print('happy')
    else:
        print('sad')