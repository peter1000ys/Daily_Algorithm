import sys

input = sys.stdin.readline

S = int(input())

total = 0
cnt = 0

while True:
    total += cnt

    if total > S:
        break
    else:
        cnt += 1
print(cnt - 1)
