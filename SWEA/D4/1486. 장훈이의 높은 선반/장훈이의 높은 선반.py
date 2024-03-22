def back(x, sum):
    global min_

    if sum >= b:
        min_ = min(min_, sum-b)
        return

    if x == n:
        return

    back(x+1, sum+s[x])
    back(x + 1, sum)

T = int(input())
for tc in range(1, T+1):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    min_ = 10000
    back(0, 0)
    print(f'#{tc} {min_}')
