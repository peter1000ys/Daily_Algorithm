def omoke(x, y):
    # 오른쪽 아래 2시방향 4시방향
    dr = [0, 1, -1, 1]
    dc = [1, 0, 1, 1]

    for d in range(4):
        cnt = 1
        for i in range(1, 5):
            r, c = x + dr[d] * i, y + dc[d] * i
            if not (0 <= r < N and 0 <= c < N): break
            if arr[r][c] == 'o':
                cnt += 1
            if cnt == 5:
                return True
    return False


def start():
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':
                if omoke(x, y):
                    return 'YES'

    return 'NO'


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    print(f'#{tc} {start()}')

