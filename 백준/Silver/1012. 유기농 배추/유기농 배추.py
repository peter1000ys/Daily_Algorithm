from collections import deque

def yard(x, y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 0
    while queue:
        sx,sy = queue.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1),(0, -1)]:
            nx, ny = sx + di, sy + dj
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 0



T = int(input())
for tc in range(T):
    n,m,k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    lst = []
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1
        lst.append((x,y))

    for a, b in lst:
        if arr[a][b] == 1:
            yard(a, b)
            cnt += 1
    print(cnt)