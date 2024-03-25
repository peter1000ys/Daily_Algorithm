from collections import deque


def bfs(r, c):
    queue = deque()
    queue.append((r, c, 0))
    visited[r][c][0] = 1

    while queue:
        x, y, c = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽을 만났을 때
            if arr[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            # 옆에 0이 있으면 이동한다
            if arr[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                queue.append((nx, ny, c))
    return -1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
print(bfs(0, 0))