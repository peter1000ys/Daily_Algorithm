from collections import deque


# 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정

# 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태
# 각 원소는 해당 지점의 높이를 표시하는 자연수
def is_valid(a):
    if 0 <= a < n:
        return True
    return False


def bfs(x, y, t):
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        sr, sc = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nr, nc = sr + dr, sc + dc
            if is_valid(nr) and is_valid(nc) and visited[nr][nc] == 0 and arr[nr][nc] >= t:
                queue.append((nr, nc))
                visited[nr][nc] = 1


def find(t):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j] >= t:
                bfs(i, j, t)
                cnt += 1

    return cnt


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for t in range(100):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    result = max(result, find(t))

print(result)
