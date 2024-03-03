def check(lst):
    max_ = 1
    n = len(lst)
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if lst[i][j] == lst[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_:
                max_ = cnt

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if lst[j][i] == lst[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_:
                max_ = cnt
    return max_


N = int(input())
arr = [list(input()) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(N):
        
        if j + 1 < N:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

            result = check(arr)
            if result > ans:
                ans = result
                
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

for i in range(N):
    for j in range(N):
        if i + 1 < N:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

            result = check(arr)
            if result > ans:
                ans = result
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(ans)
