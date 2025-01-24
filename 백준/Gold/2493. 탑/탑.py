import sys

input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))

ans = [0] * n

stack = []

for i in range(n):
    while stack:
        if stack[-1][1] > buildings[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()

    stack.append((i, buildings[i]))

print(*ans)


