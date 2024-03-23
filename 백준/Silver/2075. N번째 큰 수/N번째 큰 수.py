from heapq import heappush, heappop

n = int(input())
heap = []

for i in range(n):
    arr = list(map(int, input().split()))
    # 처음에 n만큼만 입력을 받음
    if not heap:
        for num in arr:
            heappush(heap, num)
    # 그 후 그 길이를 유지하면서 새로운 값이 최솟값보다 크면 갈아줌
    else:
        for num in arr:
            if heap[0] < num:
                heappush(heap, num)
                heappop(heap)
print(heappop(heap))