import sys
import heapq
input = sys.stdin.readline

n = int(input())
total = 0
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))

while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    total = total + (a+b)
    heapq.heappush(arr, a+b)

print(total)