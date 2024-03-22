
from collections import deque


def bfs(start):

    queue = deque([start])
    visited[start] = 1
    while queue:

        node = queue.popleft()
        for x in adjl[node]:
            if not visited[x]:
                queue.append(x)
                visited[x] = visited[node] + 1




for tc in range(1, 11):
    # 연락 인원은 최대 100명, 1~100
    visited = [0] * 101
    v, start = map(int, input().split())
    adjl = [[] for _ in range(101)]
    arr = list(map(int, input().split()))
    for i in range(v//2):
        adjl[arr[i*2]].append(arr[i*2 + 1])
    bfs(start)
    a = max(visited)
    max_ = 0
    for q in range(101):
        if visited[q] == a:
            max_ = max(max_, q)
    print(f'#{tc} {max_}')