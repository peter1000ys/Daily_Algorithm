import sys
input = sys.stdin.readline

left_stack = list(input().rstrip())
right_stack = []
M = int(input())
for _ in range(M):
    command = input()
    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
        else:
            continue

    elif command[0] == 'P':
        left_stack.append(command[2])

    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
        else:
            continue

    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
        else:
            continue
while right_stack:
    left_stack.append(right_stack.pop())

print(*left_stack,sep='')