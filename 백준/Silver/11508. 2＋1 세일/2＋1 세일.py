import sys
input = sys.stdin.readline

n = int(input())

# 3개로 묶을 수 있는 개수
bundle = n // 3

arr = []
for _ in range(n):
    arr.append(int(input()))
# 큰 수부터 정렬하고 3개씩 묶으면 가장 큰 수들을 뺄 수 있지 않을까
arr.sort(reverse=True)
total = sum(arr)
for i in range(1, bundle+1):
    total -= arr[3*i-1]

print(total)