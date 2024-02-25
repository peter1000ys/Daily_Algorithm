def to_postfix(T):
    if T:
        to_postfix(left[T])
        to_postfix(right[T])
        postfix.append(node[T])


def cal_postfix(arr):
    stack = []
    for i in arr:
        if i not in '+-/*':
            stack.append(i)
        else:
            if stack:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a + b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(a / b)
                elif i == '-':
                    stack.append(a - b)
    return stack[0]


for tc in range(1, 11):
    N = int(input())
    postfix = []
    left = [0] * (N+1)
    right = [0] * (N+1)
    node = [0] * (N+1)
    for _ in range(N):
        arr = list(input().split())
        if len(arr) == 4:
            node[int(arr[0])] = arr[1]
            left[int(arr[0])] = int(arr[2])
            right[int(arr[0])] = int(arr[3])
        else:
            node[int(arr[0])] = arr[1]
    to_postfix(1)
    print(f'#{tc} {int(cal_postfix(postfix))}')