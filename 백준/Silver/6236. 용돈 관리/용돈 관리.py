import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

start = max(arr)

end = sum(arr)

while start <= end:

    k = (start + end) // 2
    cnt = 1
    remain = k

    for i in arr:

        if remain < i:
            remain = k - i
            cnt += 1
        else:
            remain -= i

    if cnt > M:
        start = k + 1

    else:
        end = k - 1
        ans = k
print(ans)
