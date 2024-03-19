import sys
input = sys.stdin.readline


def check(x):
    for i in range(x):
        if used[x] == used[i] or abs(x - i) == abs(used[x] - used[i]):
            return False
    return True


def nqueen(x):
    global cnt
    if x == n:
        cnt += 1
        return

    for i in range(n):
        used[x] = i
        if check(x):
            nqueen(x+1)


n = int(input())
used = [0] * n
cnt = 0
nqueen(0)
print(cnt)
