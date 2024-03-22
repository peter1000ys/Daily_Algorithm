from heapq import heappush, heappop
def prim(start):
    MST =[0] * n

    heap = []
    heappush(heap, (0, start))

    sum_weight = 0

    while heap:
        weight, node = heappop(heap)
        if MST[node]:
            continue

        sum_weight += weight

        MST[node] = 1

        for next_weight, next_node in adjl[node]:
            if next_weight == 0:
                continue
            if MST[next_node]:
                continue

            heappush(heap, (next_weight, next_node))
    return sum_weight

n = int(input())
m = int(input())
adjl = [[] for i in range(n)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s-1].append((w, e-1))
    adjl[e-1].append((w, s-1))
print(prim(0))