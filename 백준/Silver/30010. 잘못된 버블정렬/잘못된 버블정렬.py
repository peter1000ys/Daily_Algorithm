import sys
# 정연이가 작성한 코드
# 마지막 인덱스에 최댓값이 도달 못했는데 제외시키고 버블 정렬을 반복하는 꼴
# 고로 배열의 가장 앞자리에 최댓값이 오면 정렬을 못함
# for i in range(N - 1, 0, -1):
#
#     for j in range(i-1, -1, -1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
input = sys.stdin.readline

N = int(input())

arr = [i for i in range(1, N+1)]
arr.reverse()

print(*arr)