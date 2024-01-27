import sys

input = sys.stdin.readline

#N은 입력 받을 수열을 이루는 수
N = int(input())
#잠시 넣어 놓을 스택
stack = []
#push와 pop 과정을 순서대로 표현하는 리스트
Operator_list = []
#넣을 숫자 카운트
cnt = 1

for i in range(N):
    num = int(input())
    while cnt <= num:   #만약 입력 받은 숫자가 카운트보다 크면
        stack.append(cnt)   #같아질 때까지 하나씩 stack에 쌓아준다
        Operator_list.append('+')   #push 과정임으로 '+' 연산자 입력
        cnt += 1

    if stack[-1] == num:    #스택 가장 위 요소가 입력 받은 수와 같으면
        stack.pop()     #스택에서 뽑아준다
        Operator_list.append('-')   #pop의 과정으로 '-' 연산자 입력

    else:   #스택 안에 이미 해당 수가 있는데 가장 위가 아닌 경우
        break   #해당 수를 뽑아 올 수 없음으로 종료한다

if stack:   #중간에 종료되어 스택에 숫자가 남아있을 경우 'NO' 출력
    print('NO')
else:       
    #해당 조건들을 만족할 경우 실행된 push와 pop 모두 연산자들 출력
    print(*Operator_list, sep ='\n')
