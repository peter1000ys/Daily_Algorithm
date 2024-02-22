import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
t = N


while True:
    if t == N and cnt != 0:
        break
    else:
        if t > 9:
            a = t // 10
            b = t % 10
            t = b * 10 + (a + b) % 10
            cnt += 1

        else:
            t = t * 10 + t
            cnt += 1

print(cnt)

