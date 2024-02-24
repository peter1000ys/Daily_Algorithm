
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs():
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N  and box[nr][nc] == 0:
                queue.append((nr, nc))
                box[nr][nc] = box[r][c] + 1


N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]
queue = deque([])

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append((i, j))
bfs()
result = 0
for i in box:
    if 0 in i:
        print(-1)
        exit(0)
    if max(i) > result:
        result = max(i)
print(result-1)