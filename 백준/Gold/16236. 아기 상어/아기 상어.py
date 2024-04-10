from collections import deque

# 잡아 먹을 수 있는 물고기 탐색
def bfs(r, c):
    queue = deque()
    visited = [[0] * n for _ in range(n)]
    tlst = []
    queue.append((r, c))
    visited[r][c] = 1
    eat = 0
    while queue:
        sr, sc = queue.popleft()
        # 거리가 eat만큼 떨어진 위치는 모두 방문 했을 경우 종료
        if eat == visited[sr][sc]:
            return tlst, eat-1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == 0 and arr[nr][nc] <= shark:
                queue.append((nr, nc))
                visited[nr][nc] = visited[sr][sc] + 1
                if 0 < arr[nr][nc] < shark:
                    tlst.append((nr, nc))
                    eat = visited[nr][nc]
    # 다 돌아봤지만 먹을 수 있는 물고기가 더이상 없다
    return tlst, eat-1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 상어 기본 크기
shark = 2
# 잡아 먹은 물고기 수
cnt = 0
# 아기 상어의 위치를 찾는다
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0
ans = 0
while True:
    # 먹을 수 있는 물고기 위치 리스트와 거기까지 거리를 받아온다
    tlst, dist = bfs(ci, cj)
    # 먹을 수 있는 물고기를 못 찾는 경우로 break
    if len(tlst) == 0:
        break
    # 조건에 맞는 먹이부터 먹기 위해 정렬
    tlst.sort(key=lambda x: (x[0], x[1]))
    # 먹을 물고기 위치
    ci, cj = tlst[0]
    # 먹은 물고기 처리
    arr[ci][cj] = 0
    # 먹은 물고기 수 증가
    cnt += 1
    # 상어가 진화할 수 있는 조건을 충족
    if cnt == shark:
        shark += 1
        # 문제에는 자세히 안나와 있지만 진화하면 잡아먹은 물고기 수를 초기화해야 한다
        cnt = 0
    # 물고기 잡아 먹기 위해 이동한 거리 증가
    ans += dist
print(ans)
