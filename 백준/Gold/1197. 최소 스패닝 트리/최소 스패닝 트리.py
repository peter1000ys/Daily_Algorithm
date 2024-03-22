# 모든 정점들을 연결하는 부분 그래프 => MST = prim, kruskal
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def find_set(x):
    if parents[x] == x:

        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    
    if x == y:
        return

    if x > y:
        parents[x] = y
    else:
        parents[y] = x


V, E = map(int, input().split())
heap = []
parents = [i for i in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    heappush(heap, (w, s-1, e-1))

sum_weight = 0


while heap:
    w, s, e = heappop(heap)

    if find_set(s) == find_set(e):
        continue

    union(s, e)
    sum_weight += w

print(sum_weight)

