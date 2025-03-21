import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
student_num = int(input())

for i in range(student_num):
    sex, num = map(int,input().split())

    a = 1

    if sex == 1:

        while a*num <= len(arr):
            if arr[a*num-1] == 0:
                arr[a*num-1] = 1
            else:
                arr[a*num-1] = 0
            a += 1
    elif sex == 2:

        if arr[num-1] == 0:
            arr[num-1] = 1
        else:
            arr[num-1] = 0

        while True:
            if num-a-1 < 0 or num+a > len(arr):
                break
            else:
                if arr[num-a-1] == arr[num+a-1]:
                    if arr[num-a-1] == 0:
                        arr[num-a-1], arr[num+a-1] = 1, 1
                    else:
                        arr[num-a-1], arr[num+a-1] = 0, 0
                    a += 1
                else:
                    break

for row in range(len(arr)//20 + 1):
    print(*arr[20*row:20*(row+1)])
