from collections import deque

# f = 건물 총 층 수, g = 목적지, s = 현재 위치, u = 한번에 올라갈 수 있는 층 수
# d = 한번에 내려갈 수 있는 층 수
# 만약 도달할 수 없다면 use the stairs 출력

f, s, g, u, d = map(int, input().split())
cnt = 0
def bfs():
    global cnt
    visited = [0] * 1000001
    queue = deque()
    queue.append(s)
    visited[s] = 1
    temp = False
    while queue:
        size = len(queue)
        for i in range(size):
            x = queue.popleft()
            if x == g:
                temp = True
                return temp
            for nx in (x + u, x - d):
                if 0 < nx <= f and visited[nx] == 0:
                    queue.append(nx)
                    visited[nx] = 1
        cnt += 1
a = bfs()
if a:
    print(cnt)
else:
    print('use the stairs')