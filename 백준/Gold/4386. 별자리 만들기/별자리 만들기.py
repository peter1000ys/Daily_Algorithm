import sys
input = sys.stdin.readline
from heapq import heappush, heappop
def prim(start):
    MST = [0] * n
    heap = []
    heappush(heap, (0, start))
    sum_cost = 0
    while heap:
        cost, node = heappop(heap)

        if MST[node]:
            continue

        MST[node] = 1

        sum_cost += cost

        for next in range(n):
            if MST[next]:
                continue
            if graph[node][next] == 0:
                continue
            heappush(heap,(graph[node][next], next))
    return sum_cost


n = int(input())
graph = [[0] * n for _ in range(n)]
index = []
for _ in range(n):
    a, b = map(float, input().split())
    index.append((a,b))
for i in range(n):
    for j in range(n):
        if i != j:
            graph[i][j] = round(((index[i][0] - index[j][0])**2  + (index[i][1] - index[j][1])**2)**0.5,2)

print(prim(0))