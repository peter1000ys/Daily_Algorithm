import sys

# from collections import deque

input = sys.stdin.readline

# 처음 입력 받는 값
eq = list(input().rstrip())

# 총 계산 값
ans = 0

tmp = 1

# 감싸고 있는 괄호를 구분하기 위해 필요
stack = []

for i in range(len(eq)):
    if eq[i] == '(':
        stack.append(eq[i])
        tmp *= 2

    elif eq[i] == '[':
        stack.append(eq[i])
        tmp *= 3

    elif eq[i] == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        else:
            if eq[i-1] == '(':
                ans += tmp
            tmp //= 2
            stack.pop()

    elif eq[i] == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        else:
            if eq[i-1] == '[':
                ans += tmp
            tmp //= 3
            stack.pop()
if stack:
    print(0)
else:
    print(ans)
