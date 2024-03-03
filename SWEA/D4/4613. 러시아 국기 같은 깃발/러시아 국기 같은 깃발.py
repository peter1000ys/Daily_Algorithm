T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    max_ = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for k in range(i+1):
                cnt += arr[k].count('W')
            for k in range(i+1, j+1):
                cnt += arr[k].count('B')
            for k in range(j+1, N):
                cnt += arr[k].count('R')
            max_ = max(max_, cnt)
    print(f'#{tc} {N*M - max_}')
