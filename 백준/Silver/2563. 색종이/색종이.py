import sys

input = sys.stdin.readline

T = int(input())

board = [[0] * 100 for _ in range(100)]
cnt = 0
for tc in range(T):
    r, c = map(int, input().split())
    for i in range(10):
        for j in range(10):
            nr = r + i
            nc = c + j
            if 0 <= nr < 100 and 0 <= nc < 100:
                    board[nr][nc] = 1
            else:
                continue
for i in board:
    cnt += i.count(1)
print(cnt)
