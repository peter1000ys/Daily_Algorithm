used = []


def nm(x, path):
    if x == m:
        print(*path, sep=' ')
        return

    for i in range(1, n+1):
        if i not in used:
            used.append(i)
            nm(x+1, path + [i])
            used.pop()


n, m = map(int, input().split())
nm(0, [])