
def f(x, start):
    if x == 6:
        print(*path)
        return

    for i in range(start, k):
            path.append(s[i])
            f(x+1, i + 1)
            path.pop()


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    if k == 0:
        break
    path = []
    f(0, 0)
    print()
