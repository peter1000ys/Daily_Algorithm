n = int(input())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
arr_a.sort()
arr_b.sort(reverse=True)
answer = 0
for i in range(n):
    answer += arr_a[i] * arr_b[i]
print(answer)