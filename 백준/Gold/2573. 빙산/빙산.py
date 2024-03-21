from collections import deque
def bfs(r, c, visited):
    queue = deque([(r, c)])
    visited[r][c] = 1
    while queue:
        sr, sc = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = sr + dr, sc + dc
            if visited[nr][nc] == 0 and arr[nr][nc] > 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1


def find():
    for year in range(1, 900000):
        a = [[0]*m for _ in range(n)]
        for i in range(1, n-1):
            for j in range(1, m-1):
                if arr[i][j] == 0:
                    continue
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i+di, j + dj
                    if arr[ni][nj] == 0:
                        a[i][j] += 1

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if a[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - a[i][j])

        visited = [[0]*m for _ in range(n)]
        cnt = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if visited[i][j] == 0 and arr[i][j] > 0:
                    bfs(i, j, visited)
                    cnt += 1
                if cnt > 1:
                    return year
        if cnt == 0:
            return 0

    return -1




n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = find()
print(result)