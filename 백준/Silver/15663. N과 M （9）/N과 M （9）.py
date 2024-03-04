import sys
input = sys.stdin.readline

path = []

def NnM(x, arr):
    if x == m:
        print(*arr, sep=' ')
        return
    prev = 0
    for i in range(0,n):
        if used[i] == 0 and prev != lst[i]:
            prev = lst[i]
            used[i] = 1
            NnM(x+1, arr + [lst[i]])
            used[i] = 0


n, m = map(int, input().split())
used = [0] * (n+1)
lst = list(map(int, input().split()))
lst.sort()
NnM(0,[])

