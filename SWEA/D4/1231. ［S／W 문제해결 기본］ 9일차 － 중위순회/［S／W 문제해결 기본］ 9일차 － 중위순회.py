def inorder(T):
    if T:
        inorder(left[T])
        print(node[T], end='')
        inorder(right[T])


for tc in range(1, 11):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    node = [0] * (N + 1)

    for _ in range(N):
        arr = list(input().split())
        if len(arr) >= 2:
            node[int(arr[0])] = arr[1]
            if len(arr) >= 3:
                left[int(arr[0])] = int(arr[2])
                if len(arr) == 4:
                    right[int(arr[0])] = int(arr[3])
    print(f'#{tc}', end=' ')
    inorder(1)
    print()
