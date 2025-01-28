import sys

input = sys.stdin.readline

def back(path):

    if len(path) == m:
        print(*path)
        return

    for i in range(1, n+1):
        if i not in path:
            path.append(i)
            back(path)
            path.pop()


n, m = map(int, input().split())

back([])