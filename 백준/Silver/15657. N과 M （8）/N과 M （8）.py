import sys

input = sys.stdin.readline

def back(a, path):
    if len(path) == m:
        print(*path)
        return

    for i in range(a, n):
        back(i, path + [arr[i]])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

back(0, [])