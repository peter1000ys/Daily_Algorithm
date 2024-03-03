T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    tmp = 'Possible'
    remain = 0
    sold = 0
    for i in arr:
        made = i // M * K
        sold += 1
        remain = made - sold
        if remain < 0:
            tmp = 'Impossible'
    print(f'#{tc} {tmp}')