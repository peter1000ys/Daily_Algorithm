import sys
input = sys.stdin.readline
from collections import deque




def bfs():
    queue = deque(ans)
    cnt = 0
    while queue:
        if cnt == s:
            return
        for _ in range(len(queue)):
            sr, sc, t = queue.popleft()
            visited[sr][sc] = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = sr + dr, sc + dc
                if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and arr[nr][nc] == 0:
                    visited[nr][nc] = 1
                    arr[nr][nc] = t
                    queue.append((nr, nc, t))
        cnt += 1


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
visited = [[0] * n for _ in range(n)]
ans = []

for i in range(1, k+1):
        for j in range(n):
            for k in range(n):
                if arr[j][k] == i:
                    ans.append((j, k, i))
bfs()
print(arr[x-1][y-1])
