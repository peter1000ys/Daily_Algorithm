def nm(x, path):
    if x == m:
        print(*path, sep=' ')
        return
    prev = 0
    for i in range(0, n):
        if prev != arr[i]:
            prev = arr[i]
            nm(x+1, path + [arr[i]])


n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
nm(0, [])