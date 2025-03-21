import sys
from copy import deepcopy

input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n, d = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [[0]*n for _ in range(n)]

    if d < 0:
        d = 360+d

    if d == 360 or d == 0:
        for row in arr:
            print(*row)
    else:
        for r in range(d//45):
            for i in range(n):
                for j in range(n):
                    if j == n//2:
                        result[i][n-i-1] = arr[i][j]
                    elif i == j:
                        result[i][n//2] = arr[i][j]
                    elif j == n-i-1:
                        result[n//2][j] = arr[i][j]
                    elif i == n//2:
                        result[j][j] = arr[i][j]
                    else:
                        result[i][j] = arr[i][j]

            arr = deepcopy(result)

        for row in arr:
            print(*row)


