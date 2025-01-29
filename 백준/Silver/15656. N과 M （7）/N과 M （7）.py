import sys

input = sys.stdin.readline

def back(path):
    if len(path) == m:
        print(*path)
        return

    for i in range(0, n):
        back(path + [arr[i]])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

back([])