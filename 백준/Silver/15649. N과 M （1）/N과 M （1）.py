path = []


def NnM():
    if len(path) == m:
        print(*path, sep=' ')

        return

    for i in range(1, n+1):
        if i not in path:
            path.append(i)
            NnM()
            path.pop()


n, m = map(int, input().split())
NnM()