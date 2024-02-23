"""
N = 정점의 개수
M = 간선의 개수
V = 시작 정점

"""
from collections import deque
def dfs(n):
    visited_dfs[n] = 1
    print(n, end=' ')
    for w in adjl[n]:
        if visited_dfs[w] == 0:
            dfs(w)

def bfs(n):
    visited_bfs = [n]
    queue = deque([n])
    while queue:
        a = queue.popleft()
        print(a, end=' ')
        for w in adjl[a]:
            if w not in visited_bfs:
                visited_bfs.append(w)
                queue.append(w)


N, M, V = map(int, input().split())

adjl = [[] for _ in range(N+1)]
visited_dfs = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for i in range(N+1):
    adjl[i].sort()


dfs(V)
print()
bfs(V)