from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    cnt = 1
    visited[v] = cnt
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        for i in adjlist[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)



n,m,r = map(int,input().split())
visited = [0]*(n+1)
adjlist = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
for lst in adjlist:
    lst.sort(reverse=True)
bfs(r)
print(*visited[1:], sep='\n')