import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

def boomba(x, lst):

    if x == 1:
        return arr


    def explode(board):
        new_board = [['O']*c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    new_board[i][j] = '.'
                    for d in range(4):
                        sr, sc = i + dr[d], j + dc[d]
                        if 0 <= sr < r and 0 <= sc < c:
                            new_board[sr][sc] = '.'
        return new_board

    all_bomb = [['O']*c for _ in range(r)]
    exploded = explode(lst)
    second_exploded = explode(exploded)

    if x % 2 == 0:
        return all_bomb

    elif (x // 2) % 2 == 1:
        return exploded

    else:
        return second_exploded


r, c, n = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(r)]

ans = boomba(n, arr)

for row in ans:
    print(''.join(row))

