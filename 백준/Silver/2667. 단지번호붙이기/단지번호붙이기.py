import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(r,c):
    cnt = 1
    queue = deque([(r,c)])
    visited[r][c] = 1
    while queue:
        sr, sc = queue.popleft()
        for d in range(4):
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == '1' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr,nc))
                cnt += 1
    return cnt


n = int(input())

arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == '1' and visited[i][j] == 0:
            house_cnt = bfs(i,j)
            ans.append(house_cnt)

print(len(ans))
ans.sort()
for a in ans:
    print(a)

