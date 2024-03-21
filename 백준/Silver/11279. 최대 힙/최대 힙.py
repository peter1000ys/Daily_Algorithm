import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())

for _ in range(n):
    x = int(input())
    if x > 0:
        # 튜플 형태로 저장
        heapq.heappush(heap, (-x, x))
    elif x == 0:
        if heap:
            # 가장 작은 값은 가장 큰값의 음수 형태로 저장됨
            # 그러니 가장 작은 값의 2번째 값을 출력하게 하면 최댓값이 출력되는 것 같다
            print(heapq.heappop(heap)[1])
        else:
            print(0)