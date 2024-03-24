def back(x, sum_):
    global min_
    if sum_ >= b:
        min_ = min(min_, sum_)
        return

    if x == n:
        return

    back(x+1, sum_ + s[x])
    back(x+1, sum_)


T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    min_ = 1e9
    back(0, 0)
    print(f'#{tc} {min_ - b}')