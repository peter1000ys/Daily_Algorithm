import sys

input = sys.stdin.readline

def check():
    cnt = 0
    for a in range(5):
        if arr[a].count(0) == 5:
            cnt += 1

    for a in range(5):
        zero_cnt = 0
        for b in range(5):
            if arr[b][a] == 0:
                zero_cnt += 1
            else:
                break
        if zero_cnt == 5:
            cnt += 1

    cross_cnt = 0
    rev_cnt = 0
    for a in range(5):
        if arr[a][a] == 0:
            cross_cnt += 1
        if arr[a][4-a] == 0:
            rev_cnt += 1

    if cross_cnt == 5:
        cnt += 1
    if rev_cnt == 5:
        cnt += 1

    return cnt



def bingo(n):
    for x in range(5):
        for y in range(5):
            if arr[x][y] == n:
                arr[x][y] = 0
    return check()

arr = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        bingo_cnt = bingo(call[i][j])
        if bingo_cnt >= 3:
            print(cnt)
            exit(0)



