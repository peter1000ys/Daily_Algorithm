import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


r, c, n = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(r)]
bomb = deque([])

def bombs():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                bomb.append((i,j))

def fill_bombs():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
# 홀수 일 때 채우고, 짝수일 때 터트림
# 짝수에서 터트리고 남은 폭탄을 찾고, 홀수에서는 채우기만 하고
def boomba(x):

    if x % 2 == 0:
        bombs()
        fill_bombs()
    else:
        while bomb:
            sr, sc = bomb.popleft()
            arr[sr][sc] = '.'
            for d in range(4):
                qr, qc = sr + dr[d], sc + dc[d]
                if 0 <= qr < r and 0 <= qc < c:
                    arr[qr][qc] = '.'

    if x == n:
        return
    boomba(x+1)

boomba(1)
for row in arr:
    print(''.join(row))

