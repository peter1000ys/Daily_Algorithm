import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, R):
    if x== N:
        return

    visited[R] = x
    for i in adjl[R]:
        if visited[i] == -1:
            dfs(x+1, i)




N, M, R = map(int, input().split())
adjl = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)
for i in range(len(adjl)):
    adjl[i].sort()

dfs(0, R)
for i in range(1, len(visited)):
    print(visited[i])