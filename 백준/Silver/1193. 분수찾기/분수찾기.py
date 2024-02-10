import sys

input = sys.stdin.readline

dr = [0, 1, -1]
dc = [1, -1, 1]

N = int(input())
cnt = 1
row = 1
col = 1
d = 0
while True:
    if N == cnt:
        break

    row = row + dr[d]
    col = col + dc[d]
    cnt += 1
    if row == 1 and N != cnt:
        if cnt == 2:
            d = 1
            continue
        else:
            col += 1
            cnt += 1
            d = 1
    elif col == 1 and N != cnt:
        row += 1
        cnt += 1
        d = 2

print(f'{row}/{col}')
