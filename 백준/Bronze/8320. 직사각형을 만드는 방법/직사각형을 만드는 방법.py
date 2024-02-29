N = int(input())
cnt = 0

for W in range(1, N + 1):
    mx_h = N // W
    cnt += mx_h

for w in range(1, N + 1):
    if w * w <= N:
        cnt += 1

print(cnt // 2)
