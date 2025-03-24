import sys

input = sys.stdin.readline

h,w = map(int, input().split())

walls = list(map(int, input().split()))

left_max = [0] * w
right_max = [0] * w

left_max[0] = walls[0]

for i in range(1, w):
    left_max[i] = max(left_max[i-1], walls[i])

right_max[w-1] = walls[w-1]

for i in range(w-2, -1, -1):
    right_max[i] = max(right_max[i+1], walls[i])


water = 0

for i in range(w):
    water += min(left_max[i], right_max[i]) - walls[i]

print(water)