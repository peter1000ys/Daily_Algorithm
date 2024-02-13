import sys
input = sys.stdin.readline

N = int(input())
arr = []
stack = []
equation = list(input().rstrip())

for _ in range(N):
    arr.append(float(input()))

for x in equation:
    if x.isalpha():
        stack.append(arr[ord(x) - ord('A')]) 
    elif x in '+-*/':
        if len(stack) < 2:
            print("Error: Insufficient operands for operator.")
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
        print("Error: Invalid character in the equation.")
        sys.exit(1)


result = stack[-1]


print(f'{result:.2f}')
