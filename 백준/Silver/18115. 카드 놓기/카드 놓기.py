from collections import deque
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
stack = [i for i in range(1, n+1)]
queue = deque()
for i in range(len(arr)):
    if arr[i] == 1:
        queue.appendleft(i+1)
    elif arr[i] == 2:
        a = queue.popleft()
        queue.appendleft(i+1)
        queue.appendleft(a)
    else:
        queue.append(i+1)
print(*queue)
