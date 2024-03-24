T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    temp = 'OFF'
    for i in range(n):
        if m & (1<<i):
            temp = 'ON'

        else:
            temp = 'OFF'
            break
    print(f'#{tc} {temp}')