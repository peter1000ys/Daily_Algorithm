path = []
used = []


def f(x, sum_card):
    global max_v

    if sum_card > M:
        return

    if x == 3:
        if sum_card <= M:
            max_v = max(sum_card, max_v)

        return

    for i in range(n):
        if i not in used:
            path.append(arr[i])
            used.append(i)
            f(x+1, sum_card + arr[i])
            path.pop()
            used.pop()


n, M = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
f(0, 0)
print(max_v)