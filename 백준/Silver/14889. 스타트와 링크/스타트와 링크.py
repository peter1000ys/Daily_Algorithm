import sys

input = sys.stdin.readline

def team(start, x):
    global min_team

    if x == N//2:
        sum_team1, sum_team2 = 0, 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j] and i != j:
                    sum_team1 += arr[i][j]
                elif not visited[i] and not visited[j] and i != j:
                    sum_team2 += arr[i][j]
        min_team = min(min_team, abs(sum_team1-sum_team2))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            team(i, x+1)
            visited[i] = 0
# N 축구를 하기 위해 모인 사람, 짝수
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_team = 1000000
# N//2명으로 이루어진 팀 2개로 나눔
team(0, 0)
print(min_team)
