import sys

input = sys.stdin.readline

def back(a, path):

    if len(path) == m:
        print(*path)
        return

    for i in range(a, n+1):
        back(i, path + [i])


n, m = map(int, input().split())

back(1, [])