from collections import deque


def bfs(r,c):
    arr[r][c] = 0
    queue = deque()
    queue.append((r,c))
    cnt = 1
    while queue:
        sr, sc = queue.popleft()
        for dr, dc in ((1,0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1:
                queue.append((nr,nc))
                arr[nr][nc] = 0
                cnt += 1
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            lst.append(bfs(i, j))
lst.sort()
print(len(lst))
for i in lst:
    print(i)
