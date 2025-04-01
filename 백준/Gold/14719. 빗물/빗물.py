import sys

input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

max_left = [0] * w
max_right = [0] * w

max_left[0] = blocks[0]
max_right[-1] = blocks[-1]

for i in range(1, w):
    max_left[i] = max(max_left[i-1], blocks[i])
for j in range(w-2, -1, -1):
    max_right[j] = max(max_right[j+1], blocks[j])

ans = 0

for x in range(w):
    ans += min(max_left[x], max_right[x]) - blocks[x]

print(ans)