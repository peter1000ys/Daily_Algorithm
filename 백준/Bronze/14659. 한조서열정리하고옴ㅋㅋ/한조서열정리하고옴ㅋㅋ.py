import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
max_ = 0
for i in range(n-1):
    cnt = 0
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            cnt += 1
        elif arr[i] < arr[j]:
            max_ = max(max_, cnt)
            break
    max_ = max(max_, cnt)
print(max_)