import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, b):
    for w in adjl[i]:
        if not visited[w]:
            visited[w] = visited[i] + 1
            dfs(w, b)


n = int(input())
a, b = map(int, input().split())
m = int(input())
visited = [0] * (n+1)
cnt = 1
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    adjl[x].append(y)
    adjl[y].append(x)
dfs(a, b)
if visited[b] != 0:
    print(visited[b])
else:
    print(-1)
