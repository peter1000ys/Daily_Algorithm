from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def find_set(x):
    if parents[x] == x:
        return parents[x]
    parents[x] = find_set(parents[x])
    return parents[x]


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

heap = []
for _ in range(m):
    s, e, c = map(int, input().split())
    heappush(heap, (c, s, e))
sum_cost = 0
highest = 0
while heap:

    c, s, e = heappop(heap)

    if find_set(s) == find_set(e):
        continue
    union_set(s, e)

    sum_cost += c
    highest = c
# 최소 신장 트리는 간선 하나만 잘라도 2개로 분할 가능
# 그렇다면 간선 가중치가 가장 큰 간선을 잘라주면 될 듯
print(sum_cost - highest)