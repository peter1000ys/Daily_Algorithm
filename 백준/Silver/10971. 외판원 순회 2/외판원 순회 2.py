import sys

input = sys.stdin.readline

def sales(first, city, current, score, visited):

    global min_score

    if city == n:
        if W[current][first]:
            score += W[current][first]
            if score < min_score:
                min_score = score
        return

    for i in range(n):
        if i not in visited and W[current][i] != 0:
            sales(first, city+1, i, score+W[current][i], visited+[i])


n = int(input())
W = [list(map(int, input().split())) for _ in  range(n)]
min_score = n * 10**6

for i in range(n):
    sales(i,1, i, 0, [i])

print(min_score)