from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(start):
    INF = 1e8
    distance = [INF] * (n+1)
    distance[start] = 0
    heap = []
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


n, m, x = map(int, input().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    adjl[s].append((t, e))
way_back = dijkstra(x)
max_ = 0
for i in range(1, n+1):
    arr = dijkstra(i)
    max_ = max(max_, arr[x] + way_back[i])
print(max_)


