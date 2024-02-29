for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # 1은 N극, 2는 S극, 0은 빈칸, N극은 위에, S극은 아래에 위치
    stack = []
    cnt = 0
    # 세로로 조사 해볼 예정
    for i in range(N):
        # col 좌표
        for j in range(N):
            # row 좌표
            # 1이 나올 경우
            if table[j][i] == 1:
                # 만약 스택에 값이 있고 top 값이 2일 경우
                if stack and stack[-1] == 2:
                    # 2는 탈출했거나 다른 1과 교착 상황이니 pop 해준다
                    stack.pop()
                stack.append(1)
            # 2가 나오는 경우
            elif table[j][i] == 2:
                # 만약 스택에 값이 있고 top 값이 1인 경우
                if stack and stack[-1] == 1:
                    # 둘이 교착이 일어난 상황으로 pop 해주고 카운트를 하나 세준다
                    stack.pop()
                    cnt += 1
                stack.append(2)

        stack.clear()

    print(f'#{tc} {cnt}')
