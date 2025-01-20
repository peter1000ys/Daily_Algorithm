import sys

input = sys.stdin.readline

hint = []

trial = int(input())

for i in range(trial):
    hint.append(list(map(int, input().split())))

ans = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or a == c or b == c:
                continue
            else:
                cnt = 0
                for h in hint:
                    num = h[0]
                    strike = h[1]
                    ball = h[2]

                    strike_cnt = 0
                    ball_cnt = 0

                    if a == num // 100:
                        strike_cnt += 1
                    elif a == (num // 10) % 10 or a == num % 10:
                        ball_cnt += 1
                    if b == (num // 10) % 10:
                        strike_cnt += 1
                    elif b == num // 100 or b == num % 10:
                        ball_cnt += 1
                    if c == num % 10:
                        strike_cnt += 1
                    elif c == (num // 10) % 10 or c == num // 100:
                        ball_cnt += 1

                    if strike == strike_cnt and ball == ball_cnt:
                        cnt += 1
                if cnt == trial:
                    ans += 1

print(ans)