"""
후위 표기법으로 바꿔 계산하는 프로그램
연산자는 + 하나 뿐
입력 :
1. 각 테스트 케이스의 문자열 계산식의 길이
2. 문자열 계산식

출력 :
1. 후위 표기법으로 변환 했다가 그걸 계산한 값 출력
"""
isp = { '+': 1, '*': 2}
def to_postfix(infix, n):
    stack = []
    postfix = ''
    for i in range(n):
        if infix[i] not in '+*':
            postfix += infix[i]
        else:
            while stack and isp[stack[-1]] >= isp[infix[i]]:
                postfix += stack.pop()
            stack.append(infix[i])
    while stack:
        postfix += stack.pop()
    return cal_postfix(postfix)


def cal_postfix(postfix):
    stack = []
    for i in range(len(postfix)):
        if stack and postfix[i] in '*+':
            right = stack.pop()
            left = stack.pop()
            if postfix[i] == '+':
                stack.append(left + right)
            else:
                stack.append(left * right)
        else:
            stack.append(int(postfix[i]))
    return stack[0]


for tc in range(1, 11):
    n = int(input())
    infix = input()
    print(f'#{tc} {to_postfix(infix, n)}')