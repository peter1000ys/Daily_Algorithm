import sys

input = sys.stdin.readline

n = int(input())

# 숫자들
arr = []
# 결과 값들 저장용
stack = []

equation = list(input().rstrip())

for _ in range(n):
    arr.append(float(input()))

for x in equation:
    if x.isalpha():
        stack.append(arr[ord(x) - ord('A')])

    elif x in '-+/*':
        if len(stack) < 2:
            print('Error')
            sys.exit(1)

        b = stack.pop()
        a = stack.pop()

        if x == '-':
            stack.append(a - b)

        elif x == '+':
            stack.append(a + b)

        elif x == '*':
            stack.append(a * b)

        elif x == '/':
            stack.append(a / b)

    else:
        print('Error')
        sys.exit(1)

result = stack[-1]

print(f'{result:.2f}')
