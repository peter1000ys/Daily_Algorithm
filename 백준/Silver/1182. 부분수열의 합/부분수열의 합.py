import sys

input = sys.stdin.readline
# 수열의 숫자 수 : N, 크기가 양수인 부분 수열 중 그 수열을 다 더한 값 : S
N, S = map(int, input().split())
# 주어진 수열
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, 1 << len(arr)):
    lite_sum = []
    for j in range(len(arr)):
        if i & (1 << j):
            lite_sum.append(arr[j]) # 해당 부분 수열의 합
    if sum(lite_sum) == S:
        cnt += 1    # 부분 수열 속 원소를 다 더한 값이 S가 되는 경우의 수 카운트
print(cnt)
