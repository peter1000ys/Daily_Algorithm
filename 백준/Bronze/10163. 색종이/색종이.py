board = [[0 for i in range(101)] for j in range(101)]
n = int(input())
cnt = 1
for i in range(n):
    x, y, a, b = map(int, input().split())
    for i in range(a):
        for j in range(b):
            board[x + i][y + j] = cnt

    cnt += 1

for i in range(1, n+1):
    sum_ = 0
    for arr in board:
        sum_ += arr.count(i)
    print(sum_)