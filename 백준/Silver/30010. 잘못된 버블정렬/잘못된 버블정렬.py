import sys

input = sys.stdin.readline

N = int(input())

arr = [i for i in range(1, N+1)]
arr.reverse()
# 정연이가 작성한 코드
# for i in range(N - 1, 0, -1):
#
#     for j in range(i-1, -1, -1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(*arr)