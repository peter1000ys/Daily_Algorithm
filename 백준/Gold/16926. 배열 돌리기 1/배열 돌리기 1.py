import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*m for _ in range(n)]

loop = min(n, m) // 2

for i in range(loop):
    deq = deque([])
    deq.clear()
    # 위쪽
    deq.extend(arr[i][i:m-i])
    # 오른쪽
    deq.extend(row[m-i-1] for row in arr[i+1:n-i-1])
    # 아래쪽
    deq.extend(arr[n-i-1][i:m-i][::-1])
    # 왼쪽
    deq.extend(row[i] for row in arr[i+1:n-i-1][::-1])

    deq.rotate(-r)

    for j in range(i, m-i):
        result[i][j] = deq.popleft()
    for j in range(i+1, n-i-1):
        result[j][m-i-1] = deq.popleft()
    for j in range(m-i-1, i-1, -1):
        result[n-i-1][j] = deq.popleft()
    for j in range(n-i-2, i, -1):
        result[j][i] = deq.popleft()

for l in result:
    print(*l)