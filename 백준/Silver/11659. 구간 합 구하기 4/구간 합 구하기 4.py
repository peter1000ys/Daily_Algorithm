import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
An = [0] * (n+1)

for i in range(1, n+1):
    An[i] += arr[i-1] + An[i-1]

for _ in range(m):
    a, b = map(int, input().split())
    print(An[b] - An[a-1])