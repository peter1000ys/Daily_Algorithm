import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(E, R):
    global cnt
    visited[R] = cnt
    cnt += 1
    for w in E[R]:
        if visited[w] == 0:
            dfs(E, w)


N, M, R = map(int, input().split())
adjl = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1
for i in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for q in adjl:
    q.sort(reverse=True)

dfs(adjl, R)

for i in range(1, N+1):
    print(visited[i])

