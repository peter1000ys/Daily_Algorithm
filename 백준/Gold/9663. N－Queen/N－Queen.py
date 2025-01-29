import sys

input = sys.stdin.readline

n = int(input())

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(x - i) == abs(row[x] - row[i]):
            return False
    return True

def nqueen(x):

    global cnt

    if x == n:
        cnt += 1
        return

    for i in range(n):
        row[x] = i
        if check(x):
            nqueen(x+1)

row = [0] * n

cnt = 0

nqueen(0)
print(cnt)
