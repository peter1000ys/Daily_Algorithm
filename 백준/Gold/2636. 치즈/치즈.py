from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
min_ = n*m
def is_valid(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False


def left():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return True
    return False


def bfs(r, c):
    queue = deque()
    visited[r][c] = 1
    queue.append((r, c))

    while queue:
        sr, sc = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = sr + dr, sc + dc
            if is_valid(nr, nc) and visited[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
                elif arr[nr][nc] == 1:
                    visited[nr][nc] = 2


while True:
    temp = left()

    if not temp:
        break

    visited = [[0] * m for _ in range(n)]

    bfs(0, 0)
    cnt += 1
    ccnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 2:
                arr[i][j] = 0
                ccnt += 1
    min_ = min(ccnt, min_)

print(cnt)
print(min_)


