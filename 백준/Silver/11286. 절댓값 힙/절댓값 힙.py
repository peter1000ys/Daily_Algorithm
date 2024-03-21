import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    x = int(input())
    if x != 0:
        # 튜플 형태로 저장
        # 처음 값을 절댓값으로 해서 저장해주면 절댓값이 작은 수부터 출력하지 않을까
        heapq.heappush(heap, (abs(x), x))
    elif x == 0:
        if heap:

            print(heapq.heappop(heap)[1])
        else:
            print(0)