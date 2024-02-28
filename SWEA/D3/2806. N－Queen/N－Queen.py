def cross(x):
    for i in range(x):
        if used[x] == used[i] or abs(x - i) == abs(used[x] - used[i]):
            return False

    return True


def n_queen(x):
    global cnt
    if x == N:
        cnt += 1
        return

    for i in range(N):
        used[x] = i
        if cross(x):
            n_queen(x+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    used = [0] * N
    cnt = 0
    n_queen(0)
    print(f'#{tc} {cnt}')