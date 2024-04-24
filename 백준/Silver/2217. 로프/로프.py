k = int(input())
arr = []

for _ in range(k):
    arr.append(int(input()))
arr.sort()
ans = []
for x in arr:
    ans.append(x*k)
    k -= 1
print(max(ans))