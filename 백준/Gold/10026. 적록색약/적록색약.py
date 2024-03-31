from collections import deque
import sys
input = sys.stdin.readline
def is_valid(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    return False
def bfs1(r, c, t):
    queue = deque()
    queue.append((r,c))
    visited1[r][c] = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny = x+dx, y+dy
            if is_valid(nx, ny) and visited1[nx][ny] == 0 and arr[nx][ny] == t:
                queue.append((nx, ny))
                visited1[nx][ny] = 1


def bfs2(r, c, t):
    que = deque()
    que.append((r,c))
    visited2[r][c] = 1
    while que:
        x,y = que.popleft()
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx,ny = x+dx, y+dy
            if is_valid(nx, ny) and visited2[nx][ny] == 0:
                if arr[nx][ny] == t or (arr[nx][ny] == "R" and t == "G") or (arr[nx][ny] == "G" and t == "R"):
                    que.append((nx, ny))
                    visited2[nx][ny] = 1


n = int(input())

arr = [list(input()) for _ in range(n)]

visited1 = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]
cnt1, cnt2 = 0, 0
for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs1(i, j, arr[i][j])
            cnt1 += 1
        if visited2[i][j] == 0:
            bfs2(i, j, arr[i][j])
            cnt2 += 1
print(cnt1, cnt2)