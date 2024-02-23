T = int(input())
for tc in range(1, T + 1):
    # 0보다 크고 1미만인 십진수 N
    N = float(input())
    ans = ''
    # N이 0이 아닌 동안
    while N != 0:
        # N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면
        for i in range(1, 13):
            # N이 0이 되면 반복문 종료
            if N == 0:
                break
            else:
                # N의 값이 해당 소숫점 아래 이진수의 값보다 크면 빼주고
                if N >= 2 ** (-i):
                    N -= 2 ** (-i)
                    ans += '1'
                # 아니면 넘어감
                else:
                    ans += '0'
        # 3자리 이상이 필요한 경우에는 ‘overflow’를 출력
        if N < 2 ** (-12) and N != 0:
            ans = 'overflow'
            break
    print(f'#{tc} {ans}')
