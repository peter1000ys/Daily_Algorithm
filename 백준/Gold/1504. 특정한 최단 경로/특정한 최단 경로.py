from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def dijkstra(start):
    distance = [INF] * (n + 1)
    heap = []
    distance[start] = 0
    heappush(heap, (0, start))
    while heap:
        dist, node = heappop(heap)
        if distance[node] < dist:
            continue

        for next_dist, next_node in adjl[node]:
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))
    return distance
n, e = map(int, input().split())
adjl = [[] for _ in range(n+1)]
INF = 16e8
for _ in range(e):
    a,b,c = map(int, input().split())
    adjl[a].append((c, b))
    adjl[b].append((c, a))
v1, v2 = map(int, input().split())
lst = dijkstra(1)
v1_lst = dijkstra(v1)
v2_lst = dijkstra(v2)

v1_path = lst[v1] + v1_lst[v2] + v2_lst[n]
v2_path = lst[v2] + v2_lst[v1] + v1_lst[n]

ans = min(v1_path, v2_path)
if ans < INF:
    print(ans)
else:
    print(-1)