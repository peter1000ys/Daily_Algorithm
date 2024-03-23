n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
# 몇 번을 연속으로 밟았는지 0, 1, 2 로 나눠 계산
dp = [[0]*3 for i in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + arr[i-1]
    dp[i][2] = dp[i-1][1] + arr[i-1]
# 마지막 칸에서 0칸은 해당 칸을 밟지 않는 것이니 제외
print(max(dp[n][1:3]))