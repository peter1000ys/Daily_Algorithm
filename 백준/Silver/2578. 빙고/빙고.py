import sys

input = sys.stdin.readline
def bingo(point):
    for x in range(5):
        for y in range(5):
            if board[x][y] == point:
                board[x][y] = 0

def bingo_check():
    cnt = 0
    # 가로 줄 체크
    for x in range(5):
        row = True
        for y in range(5):
            if board[x][y] == 0:
                continue
            else:
                row = False
                break
        if row:
            cnt += 1

    # 세로줄 체크
    for y in range(5):
        col = True
        for x in range(5):
            if board[x][y] == 0:
                continue
            else:
                col = False
                break
        if col:
            cnt += 1

    # 대각선 체크
    side_1 = True
    for i in range(5):
        if board[i][i] == 0:
            continue
        else:
            side_1 = False
    if side_1:
        cnt += 1

    side_2 = True
    for i in range(5):
        if board[i][4-i] == 0:
            continue
        else:
            side_2 = False
    if side_2:
        cnt += 1

    return cnt


board = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
for x in range(5):
    for y in range(5):
        bingo(ans[x][y])
        cnt += 1
        if cnt > 11:
            if bingo_check() > 2:
                print(cnt)
                exit(0)