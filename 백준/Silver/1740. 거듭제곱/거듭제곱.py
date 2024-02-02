import sys

input = sys.stdin.readline

# 이진수로 변환
bit = bin(int(input()))[2:]

ans = 0

for i in range(len(bit)):
    # 이진수는 문자열 형태로 저장되어 있음으로 정수로 변환
    if int(bit[i]) == 1:
        # 이진수에서 1인 부분만 3제곱을 해줌
        ans += 3 ** (len(bit) - i - 1)
print(ans)
