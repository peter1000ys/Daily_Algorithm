def nm(x, start, path):
    if x == m:
        print(*path, sep=' ')
        return
    prev = 0
    for i in range(start, n):
        if used[i] == 0 and prev != arr[i]:
            prev = arr[i]
            used[i] = 1
            nm(x+1, i+1, path + [arr[i]])
            used[i] = 0


n, m = map(int, input().split())
used = [0] * (n+1)
arr = list(map(int, input().split()))

arr.sort()
nm(0,0, [])