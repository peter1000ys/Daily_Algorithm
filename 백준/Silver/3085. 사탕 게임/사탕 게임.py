import sys

input = sys.stdin.readline


def check(arr):
    n = len(arr)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > ans:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > ans:
                ans = cnt
    return ans


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            a = check(arr)
            if a > result:
                result = a

            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i + 1 < N:
            arr[i][j], arr[i + 1][j] = arr[i+1][j], arr[i][j]

            a = check(arr)
            if a > result:
                result = a

            arr[i][j], arr[i + 1][j] = arr[i+1][j], arr[i][j]

print(result)
