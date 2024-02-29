"""
corridor 발생 조건
end / 2 값이 다른 값 start 보다 크거나 같을 경우

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    hall = [0] * 400
    for _ in range(N):

        s, e = map(int, input().split())

        # 아랫방을 윗방으로 변경
        if s % 2 == 0: s -= 1
        if e % 2 == 0: e -= 1

        if s > e: s, e = e, s
        for i in range(s, e + 1):
            hall[i] += 1

    print(f'#{tc} {max(hall)}')
