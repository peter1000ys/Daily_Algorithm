import sys

input = sys.stdin.readline

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def open_all():
    for x in range(n):
        for y in range(n):
            if ans[x][y] == '*':
                board[x][y] = '*'

def check(i, j):
    cnt = 0

    for a in range(8):
        if 0 <= i + dx[a] < n and 0 <= j + dy[a] < n:
            if ans[i+dx[a]][j+dy[a]] == '*':
                cnt += 1
    return cnt


n = int(input())

ans = [list(input().rstrip()) for _ in range(n)]
board = [list(input().rstrip()) for _ in range(n)]

for x in range(n):
    for y in range(n):
        if board[x][y] == 'x':
            board[x][y] = check(x, y)
            if ans[x][y] == '*':
                open_all()

for row in board:
    print(*row, sep='')