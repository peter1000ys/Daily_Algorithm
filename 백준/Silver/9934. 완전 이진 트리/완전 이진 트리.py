import sys
input = sys.stdin.readline
def tree(arr, x):
    mid = len(arr) // 2
    ans[x].append(arr[mid])
    if len(arr) == 1:
        return
    tree(arr[:mid], x + 1)
    tree(arr[mid+1:], x + 1)

K = int(input())
arr = list(map(int, input().split()))
ans = [[] for _ in range(K)]
tree(arr, 0)
for i in range(K):
    print(*ans[i])
