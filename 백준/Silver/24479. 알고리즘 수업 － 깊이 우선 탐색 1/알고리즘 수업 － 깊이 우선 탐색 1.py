import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(E, R):
    global cnt
    visited[R] = cnt
    cnt += 1
    for w in E[R]:
        if not visited[w]:
            dfs(E, w)


V, E, R = map(int, input().split())
visited = [0] * (V + 1)
adjl = [[] for _ in range(V + 1)]
cnt = 1
for _ in range(E):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
for i in adjl:
    i.sort()

if not visited[R]:
    dfs(adjl, R)
    for i in range(1, V+1):
        print(visited[i])
