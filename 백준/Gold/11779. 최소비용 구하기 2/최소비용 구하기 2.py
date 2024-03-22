from heapq import heappush, heappop
import sys
input = sys.stdin.readline
# 모든 도시를 들릴 필요 없네 = 다익스트라
def dijkstra(start):
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
                nodes[next_node] = node
                heappush(heap, (new_dist, next_node))

n = int(input())
m = int(input())
INF = 1e9
distance = [INF] * (n+1)

adjl = [[] for i in range(n+1)]
for i in range(m):
    s, e, c = map(int, input().split())
    adjl[s].append((c,e))


a, b = map(int, input().split())
nodes = [a] *(n+1)
dijkstra(a)
print(distance[b])
path = [b]
now = b
while now != a:
    now = nodes[now]
    path.append(now)
path.reverse()
print(len(path))
print(*path,sep=' ')
