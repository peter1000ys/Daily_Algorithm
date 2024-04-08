import sys
input = sys.stdin.readline


def dfs(r, c):
    if dp[r][c] == -1:
        dp[r][c] = 0
        for dr, dc in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if arr[nr][nc] > arr[r][c]:
                dp[r][c] += dfs(nr, nc)
    return dp[r][c]


m,n = map(int, input().split())
arr = [[0] * (n+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(m)] + [[0] * (n+2)]
dp = [[-1] * (n+2) for _ in range(m+2)]
dp[1][1] = 1
print(dfs(m, n))