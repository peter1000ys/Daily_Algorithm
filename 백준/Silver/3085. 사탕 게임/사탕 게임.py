def check(arr):
    max_ = 0
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_:
                max_ = cnt
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if arr[j-1][i] == arr[j][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_:
                max_ = cnt
    return max_


n = int(input())
arr = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            result = check(arr)
            if result > ans:
                ans = result

            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

        if i + 1 < n:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

            result = check(arr)
            if result > ans:
                ans = result

            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
print(ans)