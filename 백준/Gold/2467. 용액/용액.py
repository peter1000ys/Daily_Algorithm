n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1
a, b = 0, 0
min_sum = abs(arr[left] + arr[right])
while left < right:
    sum_ = arr[left] + arr[right]

    if abs(sum_) <= min_sum:
        a = arr[left]
        b = arr[right]
        min_sum = abs(sum_)
    # 음수 쪽이 더 작았다는 뜻
    if sum_ <= 0:
        left += 1
    else:
        right -= 1

print(a, b)