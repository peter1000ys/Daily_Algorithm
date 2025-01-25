import sys

input = sys.stdin.readline



def dfs(n):
    visit[n] = 1

    for w in adjl[n]:
        if visit[w] == 0:
            visit[w] = 1
            dfs(w)

n = int(input())
m = int(input())
adjl = [[] for _ in range(n+1)]
visit = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())

    adjl[a].append(b)
    adjl[b].append(a)

dfs(1)

cnt = 0

for i in range(n+1):
    if visit[i] == 1:
        cnt += 1

print(cnt-1)