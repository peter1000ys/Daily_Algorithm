
# n = 총 카드 수, m = 카드 합체를 하는 횟수
n, m = map(int, input().split())
# 카드들 모음
arr = list(map(int, input().split()))

for _ in range(m):
    arr.sort()
    sum_ = arr[0] + arr[1]
    arr[0] = sum_
    arr[1] = sum_

print(sum(arr))