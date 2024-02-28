T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: (x[1], x[0]))
    cnt = 1
    start = arr[0][1]
    for i in arr:
        if i[0] >= start:
            cnt += 1
            start = i[1]
    print(f'#{tc} {cnt}')