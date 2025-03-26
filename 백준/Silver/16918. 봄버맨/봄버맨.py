import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


r, c, n = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]

# 홀수 일 때 채우고, 짝수일 때 터트림
# 짝수에서 터트리고 남은 폭탄을 찾고, 홀수에서는 채우기만 하고
def boomba(x, board):
    if x == 1:
        return board
    def explode(board):
        new_board = [['O']*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    new_board[i][j] = '.'
                    for d in range(4):
                        qr, qc = i + dr[d], j + dc[d]
                        if 0 <= qr < r and 0 <= qc < c:
                            new_board[qr][qc] = '.'
        return new_board

    all_filled = [['O']*c for _ in range(r)]
    first_explode = explode(board)
    second_explode = explode(first_explode)

    if x%2 == 0:
        return all_filled
    elif (x//2)%2 == 1:
        return first_explode
    else:
        return second_explode

ans = boomba(n, arr)
for row in ans:
    print(''.join(row))


