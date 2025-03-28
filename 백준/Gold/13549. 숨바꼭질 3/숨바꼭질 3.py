import sys
import heapq

input = sys.stdin.readline

def subin(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue
        for n in (now+1, now-1, 2*now):
            if 0 <= n <= limit:
                cost = dist
                if n != 2*now:
                    cost = dist+1
                if cost < distance[n]:
                    distance[n] = cost
                    queue.append((cost,n))

# 수빈이 위치 N, 동생의 위치 K
N, K = map(int, input().split())
# 걷는 다면 1초 후 1칸 씩 좌우로 이동, 순간이동은 0초 후 2배수 위치로 이동
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하는 프로그램
INF = int(1e9)
limit = 10**5
distance = [INF]*(limit+1)

subin(N)
print(distance[K])

