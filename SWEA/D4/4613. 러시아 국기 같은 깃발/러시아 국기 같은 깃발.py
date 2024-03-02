T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    max_ = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for s in range(i+1):
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            for s in range(j+1, N):
                cnt += arr[s].count('R')
            max_ = max(max_, cnt)
    print(f'#{tc} {N*M - max_}')