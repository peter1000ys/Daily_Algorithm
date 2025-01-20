import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))


for x in range(-999, 10000):
    for y in range(-999, 10000):
        if arr[0]*x + arr[1]*y == arr[2]:
            if arr[3]*x + arr[4]*y == arr[5]:
                print(x, y)
                break
    else:
        continue
    break




