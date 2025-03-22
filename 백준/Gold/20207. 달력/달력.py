import sys

input = sys.stdin.readline

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
arr = [0] * 367
sorted_data = sorted(data, key=lambda x : (x[0], -x[1]))

for d in sorted_data:
    for i in range(d[0], d[1]+1):
        arr[i] += 1

cnt = 0
max = 0
ans = 0
for i in arr:
    if i != 0:
       cnt += 1
       if i > max:
           max = i

    else:
        ans += (max*cnt)
        max, cnt = 0, 0

print(ans)
