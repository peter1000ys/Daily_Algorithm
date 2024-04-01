from collections import deque


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0<= nx < h and 0<= ny < w and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = 1


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * (w) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    print(cnt)