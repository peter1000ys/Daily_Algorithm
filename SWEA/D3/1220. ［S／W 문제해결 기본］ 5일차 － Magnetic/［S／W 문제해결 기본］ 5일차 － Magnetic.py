for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # 1은 N극, 2는 S극, 0은 빈칸, N극은 위에, S극은 아래에 위치
    stack = []
    cnt = 0
    for i in range(100):
        for j in range(100):
            if table[j][i] == 1:
                if stack and stack[-1] == 2:
                    stack.pop()
                stack.append(1)
            elif table[j][i] == 2:
                if stack and stack[-1] == 1:
                    stack.pop()
                    cnt += 1
                stack.append(2)
        stack.clear()

    print(f'#{tc} {cnt}')
