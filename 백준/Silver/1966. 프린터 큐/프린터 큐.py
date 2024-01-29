import sys

input = sys.stdin.readline

test_case = int(input())


for _ in range(test_case):
    cnt = 0
    N, M = map(int,input().split())
    importance = list(map(int, input().split()))

    while importance:
        max_num = max(importance)
        front = importance.pop(0)
        M -= 1

        if front == max_num:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            importance.append(front)
            if M < 0:
                M = len(importance) - 1
