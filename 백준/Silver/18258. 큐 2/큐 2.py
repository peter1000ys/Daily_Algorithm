import sys
from collections import deque


input = sys.stdin.readline

arr = deque([])

line = int(input())


for _ in range(line):
    command = input().split()
    if command[0] == 'push':
        arr.append(int(command[1]))

    elif command[0] == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)

    elif command[0] == 'size':
        print(len(arr))

    elif command[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)

    elif command[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)

    elif command[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)


