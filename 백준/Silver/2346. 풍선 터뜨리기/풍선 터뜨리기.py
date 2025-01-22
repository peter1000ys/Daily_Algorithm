import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
deq = deque(list(x for x in range(1, n+1)))

ans = []

ans.append(1)

while len(ans) != n:

    num = arr[deq[0] - 1]

    if num > 0:
        deq.popleft()
        for i in range(num-1):
            deq.append(deq.popleft())

    elif num < 0:
        deq.popleft()
        deq.appendleft(deq.pop())
        for i in range(abs(num)-1):
            deq.appendleft(deq.pop())

    ans.append(deq[0])

print(*ans)



