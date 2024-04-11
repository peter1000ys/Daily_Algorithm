from collections import deque


def test(r, c):
    global ans
    for i in range(n):
        for j in range(n):
            for e in range(1, k+1):
                a = arr[i][j]
                arr[i][j] -= e
                ans = max(bfs(r, c), ans)
                arr[i][j] = a


def is_valid(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def bfs(r, c):
    q = deque()
    q.append((r,c))
    visited = [[0]*n for _ in range(n)]
    visited[r][c] = 1
    max_v = 1
    while q:
        sr, sc = q.popleft()
        for dr, dc in ((1,0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = sr + dr, sc + dc
            if is_valid(nr, nc) and arr[nr][nc] < arr[sr][sc]:
                visited[nr][nc] = visited[sr][sc] + 1
                q.append((nr, nc))
                max_v = max(max_v, visited[nr][nc])

    return max_v


T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    max_ = 1
    arr = []
    ans = 0
    for _ in range(n):
        re = list(map(int, input().split()))
        arr.append(re)
        max_ = max(max_, max(re))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_:
                test(i, j)

    print(f'#{tc} {ans}')