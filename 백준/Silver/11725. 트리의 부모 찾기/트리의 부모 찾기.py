import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x):

    for i in adjl[x]:
        if parentNode[i] == 0:
            parentNode[i] = x
            dfs(i)
# 노드의 개수
n = int(input())

# 연결선
adjl = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)

parentNode = [0] * (n+1)

dfs(1)
print(*parentNode[2:], sep=  '\n')