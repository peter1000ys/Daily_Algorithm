path = []



def NnM(x):
    if x == m:
        print(*path, sep=' ')
        return

    for i in range(0, n):
        if arr[i] not in path:
            path.append(arr[i])
            NnM(x + 1)
            path.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
NnM(0)
