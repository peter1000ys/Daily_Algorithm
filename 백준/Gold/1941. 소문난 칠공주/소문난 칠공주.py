from collections import deque


def bfs(r, c):
    cnt = 1
    queue = deque()
    v = [[0] * 5 for _ in range(5)]
    queue.append((r, c))
    v[r][c] = 1
    while queue:
        sr, sc = queue.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = sr + di, sc + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v[ni][nj] == 0 and vv[ni][nj] == 1:
                queue.append((ni, nj))
                v[ni][nj] = 1
                cnt += 1
    return cnt == 7



def check():

    for i in range(5):
        for j in range(5):
            if vv[i][j] == 1:
                return bfs(i, j)


def dfs (x, cnt, scnt):
    global ans
    if cnt > 7:

        return

    if x == 25:

        if cnt == 7 and scnt >= 4:

            if check():

                ans += 1

        return

    vv[x//5][x%5] = 1
    dfs(x+1, cnt + 1, scnt + int(arr[x//5][x%5] == 'S'))
    vv[x//5][x%5] = 0
    dfs(x+1, cnt, scnt)


ans = 0
arr = [input() for _ in range(5)]
vv = [[0] * 5 for _ in range(5)]
dfs(0, 0, 0)
print(ans)