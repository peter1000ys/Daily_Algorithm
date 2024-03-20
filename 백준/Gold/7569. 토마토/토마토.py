from collections import deque

def bfs(alst):
    global cnt
    queue = deque(alst)

    while queue:
        size = len(queue)
        for _ in range(size):
            sz, sx, sy = queue.popleft()
            for dz, dx, dy in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                nz, nx, ny = sz + dz, sx + dx, sy + dy
                if 0 <= nz < h and 0 <= nx < m and 0 <= ny < n and visited[nz][nx][ny] == 0 and arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    visited[nz][nx][ny] = 1
                    queue.append((nz, nx, ny))
        cnt += 1


n, m, h = map(int, input().split())
arr = []
for _ in range(h):
    lst = [list(map(int, input().split())) for _ in range(m)]
    arr.append(lst)
visited = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(h)]
a = []
cnt = -1
for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1:
                a.append((i, j, k))
                visited[i][j][k] = 1
bfs(a)

temp = cnt
for q in arr:
    for t in q:
        if 0 in t:
            temp = -1


print(temp)