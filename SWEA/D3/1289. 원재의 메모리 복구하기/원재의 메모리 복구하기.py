T = int(input())

for tc in range(1, T + 1):
    arr = list(input())
    cnt = 0
    while '1' in arr:
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] != arr[i - 1]:
                for j in range(i, len(arr)):
                    arr[j] = arr[i - 1]
                cnt += 1
        if '0' not in arr:
            cnt += 1
            break
    print(f'#{tc} {cnt}')
