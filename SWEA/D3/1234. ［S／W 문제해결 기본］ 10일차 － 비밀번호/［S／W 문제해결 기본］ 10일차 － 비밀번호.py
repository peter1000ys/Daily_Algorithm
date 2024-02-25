for tc in range(1, 11):
    t, password = input().split()
    stack = []
    for i in password:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print(f'#{tc}', end=' ')
    print(*stack, sep='')