used = []


def back(x, path):
    if x == n:
        print(*path, sep=' ')
        return

    for i in range(1, n+1):
        if i not in used:
            used.append(i)
            back(x+1, path + [i])
            used.pop()

n = int(input())
back(0, [])