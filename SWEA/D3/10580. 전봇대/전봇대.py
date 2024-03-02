T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = []
    for _ in range(n):
        a = list(map(int, input().split()))
        arr.append(a)
    arr.sort(key=lambda x: x[1])
    cnt = 0
    for i in range(n-1, 0, -1):
        for j in range(i-1,-1,-1):
            if arr[i][0] < arr[j][0]:
                cnt += 1
    print(f'#{tc} {cnt}')