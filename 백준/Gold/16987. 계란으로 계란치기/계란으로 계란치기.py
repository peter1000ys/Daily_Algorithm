n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_ = 0


def egg(x, cnt):
    global max_
    if x == n or n - cnt <= 1:
        if cnt > max_:
            max_ = cnt

        return

    if arr[x][0] <= 0:
        egg(x+1, cnt)

        return

    for i in range(n):
        if x == i or arr[i][0] <= 0:
            continue
        else:
            arr[x][0] -= arr[i][1]
            arr[i][0] -= arr[x][1]
            egg(x+1, cnt + int(arr[x][0] <= 0) + int(arr[i][0] <= 0))
            arr[x][0] += arr[i][1]
            arr[i][0] += arr[x][1]
egg(0, 0)
print(max_)