import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(t):

    for w in adjl[t]:
        if visit[w] == 0:
            visit[w] = t
            dfs(w)


n = int(input())
adjl = [[] for _ in range(n+1)]
visit = [0] * (n+1)

visit[1] = 1

for _ in range(n-1):
    a, b = map(int,input().split())

    adjl[a].append(b)
    adjl[b].append(a)

dfs(1)

for i in range(2, n+1):
    print(visit[i])