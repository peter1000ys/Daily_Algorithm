path = []
cnt = 0
n, s = map(int, input().split())
arr = list(map(int, input().split()))


def Hap(start):
    global cnt

    if path and sum(path) == s:
        cnt += 1

    if start == n:
        return

    for i in range(start, n):
        path.append(arr[i])
        Hap(i+1)
        path.pop()

Hap(0)
print(cnt)