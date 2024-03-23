n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
cnt = 0

sum_ = arr[0]
while True:

    if sum_ < m:
        end += 1
        if end >= n:
            break
        sum_ += arr[end]

    elif sum_ == m:
        cnt += 1
        sum_ -= arr[start]
        start += 1

    else:
        sum_ -= arr[start]
        start += 1

print(cnt)


