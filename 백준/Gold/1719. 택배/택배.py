import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# 모든 정점이 아닌 최단 경로로 이동한다 = 다익스트라
def dijkstra(start):
    INF = 2e6
    distance = [INF for _ in range(n + 1)]
    prev_nodes = [0] * (n + 1)
    distance[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        dist, node = heappop(heap)
        if distance[node] < dist:
            continue

        for next_dist, next_node in adjl[node]:
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                prev_nodes[next_node] = node
                heappush(heap, (new_dist, next_node))
    return prev_nodes


n, m = map(int, input().split())
adjl = [[] for _ in range(n + 1)]
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    s, e, t = map(int, input().split())
    adjl[s].append((t, e))
    adjl[e].append((t, s))
for i in range(1, n + 1):

    lst = dijkstra(i)
    for j in range(1, len(lst)):
        if lst[j] == 0:
            graph[j - 1][i - 1] = '-'
        else:
            graph[j - 1][i - 1] = lst[j]

for tlst in graph:
    print(*tlst, sep=' ')
