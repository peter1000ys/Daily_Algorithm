T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = list(input().split())
    if n % 2 == 0:
        arr1 = arr[: n//2]
        arr2 = arr[n//2:]
    else:
        arr1 = arr[:n//2+1]
        arr2 = arr[n//2+1:]
    result = []
    for i in range(n):
        if i%2 == 0:
            result.append(arr1.pop(0))
        else:
            result.append(arr2.pop(0))
    print(f'#{tc}',end=' ')
    print(*result)