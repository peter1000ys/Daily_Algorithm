T = int(input())
for tc in range(1, T+1):
    board = []
    max_v = 0
    for _ in range(5):
        arr = list(input())
        max_v = max(max_v, len(arr))
        board.append(arr)

    ans = ''
    for i in range(max_v):
        for line in board:
            if i < len(line):
                ans += line[i]
    print(f'#{tc} {ans}')