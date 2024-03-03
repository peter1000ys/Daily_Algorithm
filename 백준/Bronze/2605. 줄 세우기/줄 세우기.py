n = int(input())
arr = list(map(int, input().split()))
line = []
cnt = 1
for i in arr:
    if i == 0:
        line.append(cnt)
    else:
        line.insert(len(line)-i, cnt)
    cnt += 1

print(*line)