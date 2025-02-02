import sys

input = sys.stdin.readline

n = int(input())

data = []
board = [0] * 366

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

sorted_data = sorted(data, key=lambda x : (x[0], -x[1]))

for a, b in sorted_data:
    for i in range(a, b+1):
        board[i] += 1

cnt = 0
max_h = 0
ans = 0

for x in range(1, 366):
    if board[x] > 0:
        cnt += 1
        max_h = max(max_h, board[x])
    elif board[x] == 0:
        ans += cnt * max_h
        cnt = 0
        max_h = 0
if cnt > 0:
    ans += cnt * max_h

print(ans)