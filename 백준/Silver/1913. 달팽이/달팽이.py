import sys

input = sys.stdin.readline

def solve():
    for x in range(n):
        for y in range(n):
            if arr[x][y] == m:
                print(str(x+1) + " " + str(y+1))
                return

n = int(input())
m = int(input())

num = n**2

arr = [[0]*n for _ in range(n)]

for i in range(n):

    for j in range(i, n-i):
        arr[j][i] = num
        num -= 1

    for j in range(i+1, n-i):
        arr[n-i-1][j] = num
        num -= 1

    for j in range(n-i-2, i-1, -1):
        arr[j][n-i-1] = num
        num -= 1

    for j in range(n-i-2, i, -1):
        arr[i][j] = num
        num -= 1

for row in arr:
    print(*row)
solve()