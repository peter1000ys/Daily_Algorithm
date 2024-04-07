from collections import deque


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        sr, sc = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == '#':
                queue.append((nr, nc))
                arr[nr][nc] = '.'


T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '#':
                bfs(i, j)
                cnt += 1
    print(cnt)