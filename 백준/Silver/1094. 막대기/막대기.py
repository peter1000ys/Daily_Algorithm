n = int(input())
li = [64,32,16,8,4,2,1]
ans = 0

for i in li:
    while n-i >= 0:
        n -= i
        ans += 1
print(ans)