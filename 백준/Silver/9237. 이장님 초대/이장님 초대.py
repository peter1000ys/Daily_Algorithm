n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
total = arr[0] + 1
for i in range(1, n):
    a = (arr[i] + i + 1) - total
    if a > 0:
        total += a
print(total + 1)

