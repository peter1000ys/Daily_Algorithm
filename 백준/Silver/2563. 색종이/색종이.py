board = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            board[x+i][y+j] += 1
cnt = 0
for i in board:
    cnt += i.count(0)
ans = 10000 - cnt
print(ans)