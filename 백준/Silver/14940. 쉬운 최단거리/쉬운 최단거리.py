import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(r, c):
    queue = deque([(r,c)])
    while queue:
        sr, sc = queue.popleft()

        for d in range(4):
            qr, qc = sr + dr[d], sc + dc[d]
            if 0 <= qr < n and 0 <= qc < m and arr[qr][qc] == 1 and res[qr][qc] == -1:
                res[qr][qc] = res[sr][sc] + 1
                queue.append((qr,qc))



n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
res = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            res[i][j] = 0
            bfs(i, j)
        elif arr[i][j] == 0:
            res[i][j] = 0
for row in res:
    print(*row)
