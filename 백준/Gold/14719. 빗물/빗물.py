import sys

input = sys.stdin.readline

h, w = map(int, input().split())

arr = list(map(int, input().split()))
water = 0

# 해당 건물에서 왼쪽과 오른쪽에 있는 최대 건물의 높이를 측정하고 비교하여 해당 건물이 있는 칸에 얼마나 쌓일지 분석
left_max = [0] * w
right_max = [0] * w

# 각 칸의 왼쪽 최대 높이
left_max[0] = arr[0]

for i in range(1, w):
    left_max[i] = max(left_max[i-1], arr[i])

# 각 칸의 오른쪽 최대 높이
right_max[w-1] = arr[w-1]

for i in range(w-2, -1, -1):
    right_max[i] = max(right_max[i+1], arr[i])

for i in range(w):
    water += min(left_max[i], right_max[i]) - arr[i]

print(water)
