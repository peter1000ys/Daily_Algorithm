import sys
input = sys.stdin.readline

T = int(input())

cnt = 0

for tc in range(T):
    word = input().rstrip()
    involved = []
    temp = 1
    for i in word:
        if i not in involved:
            involved.append(i)
        else:
            if i == involved[-1]:
                continue
            else:
                temp = 0

    if temp:
        cnt += 1
print(cnt)