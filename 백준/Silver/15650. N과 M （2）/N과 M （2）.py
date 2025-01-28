import sys

input = sys.stdin.readline

def back(a, path, used):

    if len(path) == m:
        print(*path)
        return

    for i in range(a, n+1):
        if i not in used:
            back(i, path+[i], used+[i])

n, m = map(int, input().split())

back(1, [], [])