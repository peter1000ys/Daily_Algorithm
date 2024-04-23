n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
count = 0
for money in arr:
    if money <= k:

        count += k // money
        k = k % money
    else:
        continue
print(count)