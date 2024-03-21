from heapq import heappush, heappop
import sys
input = sys.stdin.readline
def prim(start):
    heap = []
    # 방문한 정점
    MST = [0] * V
    # 최소 가중치 합
    sum_weight = 0

    heappush(heap, (0, start))


    while heap:
        weight, node = heappop(heap)
        # 이미 방문한 정점이면 pass
        if MST[node]:
            continue
        # 가중치를 더해 준다
        sum_weight += weight
        # 방문한 정점으로 표시
        MST[node] = 1
        # 다른 정점들 중에서
        for next_w, next_node in adjlist[node]:
            # 연결 되지 않았다면 pass
            if next_w == 0:
                continue
            # 방문한 적 있는 정점이라면 pass
            if MST[next_node]:
                continue
            # 위의 조건에 해당 사항이 없는 값들 입력
            heappush(heap, (next_w, next_node))

    return sum_weight





V, E = map(int, input().split())
# 인접 행렬로 하니 메모리 초과 발생
# g = [[0]*V for _ in range(V)]
# 인접 리스트로 바꿔줌
adjlist = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjlist[u-1].append((w,v-1))
    adjlist[v-1].append((w,u-1))

res = prim(0)
print(res)