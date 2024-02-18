import sys
input = sys.stdin.readline

def dfs(i, v):
    visited = [0] * (v+1)
    stack = []
    visited[i] = 1

    while True:

        for w in adjl[i]:
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                break
        else:
            if stack:
                i =stack.pop()
            else:
                break
    return visited.count(1)

# V = 정점(컴퓨터) 수
V = int(input())
# E = 간선(컴퓨터끼리 연결) 수
E = int(input())
# adjl = 연결 리스트
adjl = [[] for _ in range(V+1)]
for _ in range(E):
    n1, n2 = map(int, input().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
print(dfs(1, V) - 1)
