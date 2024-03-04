path = []
all_num = []

def NnM(x):
    if x == m:

        print(*path, sep=' ')
        return

    for i in range(1, n + 1):
        if path:
            if i >= path[-1]:
                path.append(i)
                NnM(x + 1)
                path.pop()
        else:
            path.append(i)
            NnM(x + 1)
            path.pop()


n, m = map(int, input().split())
NnM(0)
