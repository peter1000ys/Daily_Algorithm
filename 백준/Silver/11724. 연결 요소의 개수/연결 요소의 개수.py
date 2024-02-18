import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i, v):
    visited = [0] * (v + 1)
    visited[0] = 1
    visited[i] = 1
    stack = []
    cnt = 1
    while 0 in visited:
        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = visited.index(0)
                visited[i] = 1
                cnt += 1
    return cnt


"""
N = 정점의 개수, M = 간선의 개수
adjl = 연결 리스트
연결된 그래프들의 수를 출력
"""
N, M = map(int, input().split())
adjl = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(dfs(1, N))
