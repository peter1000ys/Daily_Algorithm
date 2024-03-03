import sys
input = sys.stdin.readline
board = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            board[a+i][b+j] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            tmp = 0
            for d in range(4):
                nr, nc = i + dr[d], j + dc[d]
                if 0 <= nr < 100 and 0 <= nc < 100 and board[nr][nc] == 1:

                    tmp += 1
            if tmp == 3:
                cnt += 1
            elif tmp == 2:
                cnt += 2
print(cnt)