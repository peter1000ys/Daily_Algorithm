import sys

input = sys.stdin.readline
#     하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

row, col = 0, 0

N = int(input())

K = int(input())


board = [[0] * N for _ in range(N)]



# 위치
d = 0

for i in range(N**2, 0, -1):
    board[row][col] = i

    nr = row + dr[d]
    nc = col + dc[d]

    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
        row = nr
        col = nc

    else:
        d += 1
        if d == 4:
            d = 0
        row += dr[d]
        col += dc[d]


for j in range(len(board)):
    print(*board[j])
    if K in board[j]:
        kx = j + 1
        ky = board[j].index(K) + 1
print(kx, ky)
