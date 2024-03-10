T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    max_ = 0
    lst = []
    for i in range(n-2):

        for j in range(i+1, n-1):

            lst.append((i, j))

    for a, b in lst:
        cnt = 0
        for x in range(a+1):
            cnt += arr[x].count('W')
        for y in range(a+1, b+1):
            cnt += arr[y].count('B')
        for z in range(b+1, n):
            cnt += arr[z].count('R')
        max_ = max(max_, cnt)

    print(f'#{tc} {n*m - max_}')


