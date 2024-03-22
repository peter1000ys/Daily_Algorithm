# 녹색은 링크입니다
from heapq import heappush, heappop


def dijkstra(r, c):
    INF = 1e9
    visited = [[INF] * n for _ in range(n)]
    heap = []
    visited[r][c] = arr[r][c]
    heappush(heap, (arr[r][c], r, c))

    while heap:
        w, sr, sc = heappop(heap)

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < n and 0 <= nc < n:
                new = w + arr[nr][nc]
                if new < visited[nr][nc]:
                    visited[nr][nc] = new
                    heappush(heap, (new, nr, nc))

    return visited[n-1][n-1]

tc = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = dijkstra(0, 0)
    print(f'Problem {tc}: {ans}')
    tc += 1
