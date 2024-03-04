path = []

def NnM(x, start):
    if x == m:
        print(*path, sep=' ')

        return

    for i in range(start, n):
        path.append(arr[i])
        NnM(x+1, i+1)
        path.pop()


n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
NnM(0,0)

