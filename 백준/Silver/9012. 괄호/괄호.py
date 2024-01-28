import sys

input = sys.stdin.readline

#테스트 데이터 수 입력
num_testdata = int(input())



for i in range(num_testdata):
    #테스트 데이터를 입력 받는다
    line = input().rstrip()
    stack = []

    for brackets in line:
        #왼쪽 괄호일 경우 스택에 추가
        if brackets == '(':
            stack.append(brackets)
        #오른쪽 스택을 입력 받을 경우 
        elif brackets == ')':
            if stack:       #스택에 내용물이 있고 
                if stack[-1] == '(':    #그 내용물이 왼쪽 괄호인 경우
                    stack.pop()     #그 값을 스택에서 빼준다
            else:   #스택에 왼쪽 괄호가 없는 경우 오른쪽 괄호를 추가해준다
                stack.append(brackets)
                break   #출력에서 'NO'가 나오게 하기 위해서
    if stack:   #스택에 내용물이 있을 경우 'NO' 출력
        print('NO')
    else:       #스택이 비어있을 경우 VPS를 만족, 'YES' 출력
        print('YES')