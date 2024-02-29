def find_point(x, y, a, b):
    dr = [1, -1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, -1, -1, 1, 1]
    for d in range(8):
        nr = x + dr[d]
        nc = y + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == a:
                t = 2
                while True:
                    nr, nc = x + dr[d] * t, y + dc[d] * t
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] == b:
                            for i in range(t+1):
                                nr, nc = x + dr[d] * i, y + dc[d] * i
                                board[nr][nc] = b
                            break
                        elif board[nr][nc] == 0:
                            break
                        else:
                            t += 1
                    else:
                        break


T = int(input())
sr = [0, 0, 1, 1]
sc = [0, 1, 1, 0]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    q, w = N // 2 - 1, N // 2 - 1
    for d in range(4):
        nq, nw = q + sr[d], w + sc[d]
        if d % 2 == 0:
            board[nq][nw] = 2
        else:
            board[nq][nw] = 1

    for _ in range(M):
        r, c, color = map(int, input().split())

        if color == 1:
            find_point(r-1, c-1, 2, 1)
        else:
            find_point(r-1, c-1, 1, 2)

    one, two = 0, 0

    for i in board:
        one += i.count(1)
        two += i.count(2)

    print(f'#{tc} {one} {two}')