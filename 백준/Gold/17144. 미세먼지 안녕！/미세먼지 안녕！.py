from collections import deque
import sys
input = sys.stdin.readline

def bfs(lst):
    visited = [[0] * c for _ in range(r)]
    queue = deque(lst)
    while queue:
        for _ in range(len(queue)):
            si, sj = queue.popleft()
            cnt = 0
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = si + di, sj + dj
                if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                    visited[ni][nj] += arr[si][sj] // 5
                    cnt += 1
            visited[si][sj] += arr[si][sj] - cnt * (arr[si][sj] // 5)
    return visited


def upper(sr, sc):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    d = 0
    e1, e2 = sr, sc + 1
    while True:
        if sr == e1 and sc == e2:
            arr[sr][sc] = 0
            break
        nr, nc = sr + dr[d], sc + dc[d]
        if 0 <= nr < e1+1 and 0 <= nc < c:
            arr[sr][sc] = arr[nr][nc]
            sr, sc = nr, nc
        else:
            d += 1



def lower(sr, sc):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    d = 0
    e1, e2 = sr, sc + 1
    while True:
        if sr == e1 and sc == e2:
            arr[sr][sc] = 0
            break
        nr, nc = sr + dr[d], sc + dc[d]
        if e1 <= nr < r and 0 <= nc < c:
            arr[sr][sc] = arr[nr][nc]
            sr, sc = nr, nc
        else:
            if d == 3:
                d = 0
            else:
                d += 1


r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

for _ in range(t):
    ans = []
    dev = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                ans.append((i, j))
            elif arr[i][j] == -1:
                dev.append((i,j))
    arr = bfs(ans)
    a1, b1 = dev.pop()
    lower(a1, b1)
    a2, b2 = dev.pop()
    upper(a2, b2)
    arr[a1][b1] = -1
    arr[a2][b2] = -1
total = 0
for line in arr:
    total += sum(line)

print(total + 2)