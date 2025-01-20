import sys

input = sys.stdin.readline

# 택희, 남규, 영훈
# 1. 남는 사탕이 없음
# 2. 남규 >= 영훈 +2
# 3. 0개 받는 사람은 없음
# 4. 택희는 짝수

# 사탕의 수가 N개 (1 <= N <= 100)

N = int(input())

ans = 0
# 남규
for a in range(1, N + 1):
    # 영휸
    for b in range(1, N):
        # 택희
        for c in range(1, N-1):
            if a+b+c == N:
                if a >= b + 2 and c%2 == 0:
                    ans += 1
print(ans)


