import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i):
    for w in adjl[i]:
        if not visited[w]:
            visited[w] = i
            dfs(w)



N = int(input())
adjl = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(visited[i])