T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = 'OFF'
    for i in range(N):
        if M & (1 << i):
            temp = 'ON'
        else:
            temp = 'OFF'
            break
    print(f'#{tc} {temp}')
