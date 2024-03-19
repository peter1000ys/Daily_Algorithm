def dongchil(x, used, cnt):
    global max_

    if cnt <= max_:
        return

    if x == n:
        max_ = max(max_, cnt)
        return

    for i in range(n):
        if i in used:
            continue
        if x == n-1 and cnt * (arr[i][x]/100) < max_:
            continue
        dongchil(x+1, used+[i], cnt * (arr[i][x]/100))


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_ = 0
    dongchil(0, [], 1)
    print(f'#{tc} {max_ * 100:.6f}')