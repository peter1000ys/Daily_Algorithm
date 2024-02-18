import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, cnt):
    visited[i] = 1
    cnt += 1
    if i == b:
        ans.append(cnt)

    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w, cnt)


n= int(input())
a, b =map(int, input().split())
m = int(input())
adjl = [[] for _ in range(n+1)]

visited = [0] * (n+1)
ans = []

for _ in range(m):
    n1, n2 = map(int, input().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)

dfs(a, 0)

if len(ans) == 0:
    print(- 1)
else:
    print(ans[0] - 1)

