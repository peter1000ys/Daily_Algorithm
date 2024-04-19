import sys
input = sys.stdin.readline
from collections import deque



T = int(input())
for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = deque()
    i = 0
    while arr:

        a = max(arr)
        if i == 0:
            ans.appendleft(a)
            arr.remove(a)
            i = 1
        else:
            ans.append(a)
            arr.remove(a)
            i = 0
    max_ = 0
    for i in range(len(ans)):
        if i >= len(ans) - 1:
            max_ = max(max_, abs(ans[i] - ans[0]))
        else:
            max_ = max(max_, abs(ans[i] - ans[i + 1]))

    print(max_)
