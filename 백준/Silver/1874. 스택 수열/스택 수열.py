import sys

input = sys.stdin.readline

N = int(input())

cnt = 1
stack = []
op = []
for i in range(N):
    M = int(input())

    while cnt <= M:
        stack.append(cnt)
        op.append('+')
        cnt += 1

    if stack[-1] == M:
        stack.pop()
        op.append('-')

if stack:
    print('NO')
else:
    print(*op, sep='\n')
