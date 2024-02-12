import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in trees:
        if mid < i:
            total += (i - mid)
        else:
            continue
    if total >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)