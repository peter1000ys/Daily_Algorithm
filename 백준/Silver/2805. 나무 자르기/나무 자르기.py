def binarysearch(m):
    start = 0
    end = max(arr)

    while start <= end:
        middle = (start + end) // 2
        total = 0
        for i in arr:
            if i > middle:
                total += (i - middle)

        if total < m:
            end = middle - 1
        elif total >= m:
            start = middle + 1
    return start - 1


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(binarysearch(m))
