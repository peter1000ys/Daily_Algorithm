T = int(input())

for tc in range(1, T+1):
    tmp = 'Possible'
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    available = 0
    sold = 0
    for customer in arr:
        made = customer // M * K
        sold += 1
        available = made - sold
        if available < 0:
            tmp = 'Impossible'
    print(f'#{tc} {tmp}')
