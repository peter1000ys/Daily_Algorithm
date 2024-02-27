
N = int(input())
visited = [0] * N
cnt = 0

def diangonal(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == abs(x - i):
            return False

    return True


def n_queen(x):
    global cnt
    if x == N:
        cnt += 1
        return

    for i in range(N):
        visited[x] = i

        if diangonal(x):
            n_queen(x+1)


n_queen(0)
print(cnt)