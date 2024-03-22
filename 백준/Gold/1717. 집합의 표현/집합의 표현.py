import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

n, m = map(int, input().split())
parents = [i for i in range(n+1)]
for _ in range(m):
    w, s, e = map(int, input().split())
    if w == 0:
        union_set(s, e)
    elif w == 1:
        if find_set(s) == find_set(e):
            print('YES')
        else:
            print('NO')