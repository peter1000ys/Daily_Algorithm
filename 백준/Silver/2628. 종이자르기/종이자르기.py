r, c = map(int, input().split())
n = int(input())
row = [0] * (c + 1)
col = [0] * (r + 1)
total = []
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0:
        row[y] = 1
    elif x == 1:
        col[y] = 1
cnt = 0
for i in range(0, len(row)-1):
    if row[i] == 1:
        total.append(cnt)
        cnt = 0
    cnt += 1
total.append(cnt)
max_r = max(total)

total = []
cnt = 0
for i in range(0, len(col)-1):
    if col[i] == 1:
        total.append(cnt)
        cnt = 0
    cnt += 1
total.append(cnt)
max_c = max(total)


print(max_r * max_c)
