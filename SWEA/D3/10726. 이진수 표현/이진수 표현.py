
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    temp = 'OFF'
    # M의 이진수에서 각각 0번째 ~ 4번째 자리에 1이 있는지 확인하고
    # 모두 1이 있을 경우 temp는 ON
    # 하나라도 0일 경우 OFF, 반복문 종료
    for i in range(N):
        if M & (1 << i):
            temp = 'ON'
        else:
            temp = 'OFF'
            break
    print(f'#{tc} {temp}')



