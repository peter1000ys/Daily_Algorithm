from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def dijkstra(start):
    INF = 1e8
    distance = [INF] * (n + 1)
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

T = int(input())
for _ in range(T):
    n, m , t = map(int, input().split())
    adjl = [[] for _ in range(n+1)]
    s, g, h = map(int, input().split())
    for _ in range(m):
        a, b, d = map(int, input().split())
        adjl[a].append((d, b))
        adjl[b].append((d, a))
    lst = dijkstra(s)
    destination = []
    for _ in range(t):
         destination.append(int(input()))
    destination.sort()
    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    gh_dist = 0
    for d in adjl[g]:
        if d[1] == h:
            gh_dist = d[0]

    for dest in destination:
        if (dist_s[dest] == dist_s[g] + gh_dist + dist_h[dest]) or (dist_s[dest] == dist_s[h] + gh_dist + dist_g[dest]):
            print(dest, end=' ')
    print()
