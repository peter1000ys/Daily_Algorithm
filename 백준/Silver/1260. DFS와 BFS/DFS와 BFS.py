import sys
from collections import deque

input = sys.stdin.readline

def dfs(n):
    dfs_visit[n] = 1
    print(n, end=" ")
    for w in adjl[n]:
        if dfs_visit[w] == 0:
            dfs_visit[w] = 1
            dfs(w)

def bfs(n):
    bfs_visit[n] = 1
    queue = deque([n])

    while queue:
        t = queue.popleft()
        print(t, end=" ")
        for x in adjl[t]:
            if bfs_visit[x] == 0:
                bfs_visit[x] = 1
                queue.append(x)



n, m, v = map(int, input().split())

adjl = [[] for _ in range(n+1)]

dfs_visit = [0]*(n+1)
bfs_visit = [0]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for list in adjl:
    list.sort()

dfs(v)
print()
bfs(v)