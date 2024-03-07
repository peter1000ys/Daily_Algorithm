from collections import deque

def bfs(tlst):
    for i, j in tlst:
        arr[i][j] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    cnt = num - 3
    for vi, vj in virus:
        queue.append((vi, vj))
        visited[vi][vj] = 1

    while queue:
        si, sj = queue.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
                cnt -= 1

    for i, j in tlst:
        arr[i][j] = 0

    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

lst = []
virus = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))
num = len(lst)
max_ = 0
for i in range(num - 2):
    for j in range(i+1, num-1):
        for k in range(j+1, num):
            tlst = [lst[i], lst[j], lst[k]]
            max_ = max(max_, bfs(tlst))
print(max_)