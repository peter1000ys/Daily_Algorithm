from collections import deque


def bfs(r, c):

    queue = deque()
    queue.append((r,c))
    result_lst = [(r, c)]
    sum_ = arr[r][c]
    visited[r][c] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                result_lst.append((nx,ny))
                sum_ += arr[nx][ny]
    if len(result_lst) > 1:
        for sr, sc in result_lst:
            arr[sr][sc] = sum_ // len(result_lst)
        return 1
    return 0


n, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
while ans <= 2000:
    visited = [[0] * n for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                temp = max(bfs(i, j), temp)
    if temp == 0:
        break
    ans += 1
print(ans)
