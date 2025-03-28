import sys
from collections import deque
input = sys.stdin.readline

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]


def saving_princess(a,b):
    queue = deque([(a,b)])
    visited[a][b] = 0
    gram = int(1e9)

    while queue:
        r, c = queue.popleft()
        if castle[r][c] == 2:
            gram = visited[r][c] + abs(n-r-1) + abs(m-c-1)
        for d in range(4):
            sr,sc = r+dr[d], c+dc[d]
            if 0 <= sr < n and 0 <= sc < m and visited[sr][sc] == -1 and castle[sr][sc] != 1:
                visited[sr][sc] = visited[r][c] + 1
                queue.append((sr, sc))
    if visited[n-1][m-1] != -1:
        return min(gram, visited[n-1][m-1])
    else:
        return gram

n,m,t = map(int, input().split())
castle = [list(map(int,input().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]


ans = saving_princess(0,0)


if ans > t:
    print('Fail')
else:
    print(ans)


