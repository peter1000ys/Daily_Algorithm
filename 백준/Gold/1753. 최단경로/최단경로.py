from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    distance = [INF] * (V + 1)
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))
    while heap:
        dist, node = heappop(heap)

        if dist > distance[node]:
            continue

        for next_dist, next_node in adjl[node]:
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))
    return distance
V, E = map(int, input().split())
start = int(input())
adjl = [[] for _ in range(V+1)]
INF = 6e9
for _ in range(E):
    u, v, w = map(int, input().split())
    adjl[u].append((w, v))
ans = dijkstra(start)
for i in range(1, V+1):
    if ans[i] == INF:
        print('INF')
    else:
        print(ans[i])