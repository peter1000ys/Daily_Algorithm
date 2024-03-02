T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    total = []
    t = 0
    while t < N:
        if (N+1)//2 + t <= N:
            a = arr[t][N-(N+1)//2 - t : N - N//2 + t]
            total.extend(a)
        else:
            a = arr[t][(N+1)//2 + t - N:N - t + N//2]
            total.extend(a)
        t += 1
    sum_ = 0
    for i in total:
        sum_ += int(i)
    print(f'#{tc} {sum_}')
