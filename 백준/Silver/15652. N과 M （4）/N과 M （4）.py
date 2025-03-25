import sys

input = sys.stdin.readline

def NnM(x, start, arr):
    if x == m:
        print(*arr)
        return

    for i in range(start, n+1):

        NnM(x+1, i, arr+[i])


n, m = map(int, input().split())

NnM(0, 1, [])