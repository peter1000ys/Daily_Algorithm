import sys

input = sys.stdin.readline

def cal_team(one):
    sum_team1, sum_team2 = 0, 0
    for i in range(len(one)):
        for j in range(i, len(one)):
            sum_team1 += arr[one[i]][one[j]] + arr[one[j]][one[i]]
    for i in range(N):
        for j in range(i, N):
            if i not in one and j not in one:
                sum_team2 += arr[i][j] + arr[j][i]
    return abs(sum_team1-sum_team2)


def team(start, link):
    global min_team

    if len(link) == N//2:
        min_team = min(cal_team(link), min_team)
        return

    for i in range(start, N):
        if i not in link:
            team(i, link+[i])
# N 축구를 하기 위해 모인 사람, 짝수
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_team = 1000000
# N//2명으로 이루어진 팀 2개로 나눔
team(0, [])
print(min_team)
