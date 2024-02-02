import sys

input = sys.stdin.readline
# 결국 물병을 2의 제곱의 값으로 만들어서 나누는 방법이 가장 좋음
N, K = map(int, input().split())
cnt = 0
# 새로 산 물병의 수를 세줌
while bin(N).count('1') > K:
    # 이진수로 만들 수 있는 개수가 K보다 같거나 작아질 때까지
    N += 1
    # 물병 추가
    cnt += 1
print(cnt)
