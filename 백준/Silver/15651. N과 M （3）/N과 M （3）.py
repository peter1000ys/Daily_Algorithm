import sys

input = sys.stdin.readline

def back(path):

    if len(path) == m:
        print(*path, sep=' ')
        return

    for i in range(1, n+1):
        back(path + [i])

n, m = map(int, input().split())

back([])
