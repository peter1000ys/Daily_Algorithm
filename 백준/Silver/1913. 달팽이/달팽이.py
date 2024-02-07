import sys

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
N = int(input())
M = int(input())

board = [[0] * N for _ in range(N)]

d = 0
row, col = 0, 0
ans_r, ans_c = 0, 0
for num in range(N ** 2, 0, -1):
    board[row][col] = num

    if board[row][col] == M:
        ans_r, ans_c = row+1, col+1

    nr = row + dr[d]
    nc = col + dc[d]

    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:

        row, col = nr, nc

    else:
        if d < 3:
            d += 1
        elif d == 3:
            d = 0
        row += dr[d]
        col += dc[d]
        continue

for x in board:
    print(*x)
print(ans_r, ans_c)