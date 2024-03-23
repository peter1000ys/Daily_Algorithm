import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))
sum_ = sum(arr[:k])
max_ = sum_
for i in range(k, n):
    sum_ = sum_ + arr[i] - arr[i-k]
    max_ = max(max_, sum_)

print(max_)
