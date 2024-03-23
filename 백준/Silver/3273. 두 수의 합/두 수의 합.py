n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
cnt = 0
start, end = 0, n-1
while start < end:
    sum_num = arr[start] + arr[end]

    if sum_num == x:
        cnt += 1
        start += 1

    elif sum_num > x:
        end -= 1

    else:
        start += 1


print(cnt)