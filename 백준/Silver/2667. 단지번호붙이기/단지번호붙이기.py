from collections import deque


def bfs(r,c):
    queue = deque()
    queue.append((r, c))
    arr[r][c] = 0
    cnt = 1

    while queue:
        si, sj = queue.popleft()
        for di, dj in ((-1, 0), (1, 0), (0,1), (0, -1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
                arr[ni][nj] = 0
                queue.append((ni, nj))
                cnt += 1
            else:
                continue
    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]


ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
    print(i)