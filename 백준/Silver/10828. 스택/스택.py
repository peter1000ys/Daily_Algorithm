import sys

input = sys.stdin.readline

N = int(input())
stack =[]

for i in range(N):
    stack_order = input().split()

    if stack_order[0] == 'push':
        stack.append(stack_order[1])
    elif stack_order[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif stack_order[0] == 'size':
        print(len(stack))
    elif stack_order[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif stack_order[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)