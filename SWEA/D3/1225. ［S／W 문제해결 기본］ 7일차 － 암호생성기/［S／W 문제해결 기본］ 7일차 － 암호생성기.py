for tc in range(1, 11):
    board = [0] * 1000000
    t = input()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        board[i] = arr[i]
    front = -1
    rear = len(arr) - 1
    x = 1
    while True:
        front += 1
        rear += 1
        board[rear] = board[front] - x
        x += 1
        if x > 5:
            x = 1
        if board[rear] <= 0:
            board[rear] = 0
            break

    lst = []
    for i in range(front + 1, rear + 1):
        lst.append(board[i])
    print(f'#{tc}', end=' ')
    print(*lst)