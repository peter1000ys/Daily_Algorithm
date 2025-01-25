import sys

input = sys.stdin.readline

n = int(input())

stack = []
circles = []

for i in range(n):
    x, r = map(int, input().split())
    circles.append((x-r, i))
    circles.append((x+r, i))

circles.sort()

for x in circles:

    if stack:
        if stack[-1][1] == x[1]:
            stack.pop()
        else:
            stack.append(x)
    else:
        stack.append(x)

if stack:
    print('NO')
else:
    print('YES')
