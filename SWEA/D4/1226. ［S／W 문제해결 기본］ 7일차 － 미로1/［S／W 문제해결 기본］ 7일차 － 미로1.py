dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(sr, sc):
    visited = [[0 for _ in range(16)]for _ in range(16)]
    queue = []
    visited[sr][sc] = 1
    queue.append((sr, sc))
    ans = 0

    while queue:

        r, c = queue.pop(0)

        if board[r][c] == 3:
            ans = 1

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]

            if 0 <= nr < 16 and 0<= nc < 16 and board[nr][nc] != 1 and not visited[nr][nc]:

                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    return ans

for tc in range(1, 11):
    t = input()
    board = []
    for _ in range(16):
        arr = list(map(int, str(input())))
        board.append(arr)

    sr, sc = 0, 0
    for i in range(16):
        for j in range(16):
            if board[i][j] == 2:
                sr, sc = i, j
    print(f' #{tc} {bfs(sr, sc)}')