import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 미로에서 1은 이동할 수 있는 칸을 나타내고,
# 0은 이동할 수 없는 칸을 나타낸다


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def bfs(a, b):
    visited = [[0] * M for _ in range(N)]
    visited[a][b] = 1
    queue = []
    ans = 0
    queue.append((a,b))
    while queue:
        r, c = queue.pop(0)

        if r == N - 1 and c == M - 1:
            ans = visited[r][c]
            break
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and board[nr][nc] == '1':
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

    return ans


N, M = map(int, input().rstrip().split())
board = []

for i in range(N):
    arr = list(input())
    board.append(arr)

print(bfs(0, 0))

