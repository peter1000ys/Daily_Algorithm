import sys

input = sys.stdin.readline

# 스택 내부 우선 순위
iis = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
# 스택 외부 우선 순위
# *가 스택 안에 위치하고 밖에 +를 만날 때는 *를 먼저 입력해야 하므로 각각의 우선 순위가 필요
ios = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}

infix = list(input().rstrip())

stack = []
postfix = ''

for i in infix:
    if i not in '+-*/()':
        postfix += i
    else:
        if i == '(':
            stack.append(i)

        elif i == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:

            while stack and iis[stack[-1]] >= ios[i]:
                postfix += stack.pop()

            stack.append(i)

while stack:
    postfix += stack.pop()

print(postfix)
