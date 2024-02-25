"""
후위 표기식 : 연산자가 피연산자 뒤에 위치하는 방법

주어진 중위 표기식을 연산자의 우선순위에 따라 괄호로 묶어준다.

"""
import sys
input = sys.stdin.readline
# 스택 밖에서의 우선 순위
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
# 스택 내부에서의 우선 순위
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

# 중위 표기식을 후위 표기식으로 바꿔 주는 함수
def to_postfix(infix, n):
    postfix = ''
    stack = []
    for i in range(n):
        if infix[i] not in '+-*/()':
            postfix += infix[i]
        else:
            if infix[i] == ')':
                while stack:
                    c = stack.pop()
                    if c == '(':
                        break
                    postfix += c
            else:
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    return postfix

infix = input().rstrip()
print(to_postfix(infix, len(infix)))

