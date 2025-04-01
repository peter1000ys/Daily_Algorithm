import sys
import heapq

def dij(start):
    queue = []
    arr[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        time, idx = heapq.heappop(queue)
        if arr[idx] < time:
            continue
        else:
            for n in (idx+1,idx-1,2*idx):
                if 0 <= n < limit:
                    cost = time
                    if n != 2*idx:
                        cost = time + 1

                    if cost < arr[n]:
                        arr[n] = cost
                        heapq.heappush(queue,(cost, n))


INF = int(1e9)
limit = 10**5 + 1
arr = [INF] * limit

n, k = map(int, input().split())
dij(n)
print(arr[k])