import sys

input = sys.stdin.readline


def back(a, path, used):
    if len(path) == m:
        print(*path)
        return

    for i in range(0, n):
        if i not in used:
            back(i, path + [arr[i]], used + [i])


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
back(1, [], [])