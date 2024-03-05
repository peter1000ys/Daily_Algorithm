import sys
sys.setrecursionlimit(10**6)


def nm(x, t, path):
    if x == m:
        print(*path, sep=' ')
        return
    prev = 0
    for i in range(0, n):
        if t <= arr[i] and prev != arr[i]:
            prev = arr[i]
            nm(x+1, arr[i], path + [arr[i]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
used = []
arr.sort()
nm(0, 0, [])