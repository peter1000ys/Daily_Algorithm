def inorder(T):
    if T:
        inorder(left[T])
        print(words[T], end='')
        inorder(right[T])


T = 10
for tc in range(1, T + 1):
    Node = int(input())
    left = [0] * (Node + 1)
    right = [0] * (Node + 1)
    words = [0 for _ in range(Node + 1)]
    for _ in range(Node):
        arr = list(map(str, input().split()))

        if len(arr) >= 2:
            words[int(arr[0])] = arr[1]
            if len(arr) >= 3:
                left[int(arr[0])] = int(arr[2])
                if len(arr) >= 4:
                    right[int(arr[0])] = int(arr[3])

    print(f'#{tc} ', end='')
    inorder(1)

    print()
