from collections import deque
import copy

def bfs(lst, arr):
    queue = deque()
    cnt = 0
    for i in lst:
        for j in range(h):
            if arr[j][i] != 0:
                queue.append((j, i, arr[j][i]))
                break
        while queue:
            r, c, weight = queue.popleft()
            for x in range(0, weight):
                for dr, dc in ((1,0), (-1,0), (0, 1), (0, -1)):
                    nr, nc = r + dr*x, c + dc*x
                    if 0 <= nr < h and 0 <= nc < w:
                        if arr[nr][nc] > 1:
                            queue.append((nr, nc, arr[nr][nc]))
                        arr[nr][nc] = 0

        cnt = sort_arr(arr)

    return cnt


def select(x, path):
    global min_
    if x == n:
        lst = copy.deepcopy(board)
        ans = bfs(path, lst)
        min_ = min(ans, min_)
        return
    for i in range(w):
        select(x+1, path + [i])


def sort_arr(arr):
    cnt = 0
    stack = []
    for i in range(w):
        for j in range(h):
            if arr[j][i] > 0:
                stack.append(arr[j][i])
                arr[j][i] = 0
                cnt += 1
        for j in range(h-1, -1, -1):
            if stack:
                arr[j][i] = stack.pop()
            else:
                break
    return cnt


T = int(input())
for tc in range(1, T+1):
    # n 떨어트리는 벽돌의 개수, w: row, h: col
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    min_ = w*h
    select(0, [])
    print(f'#{tc} {min_}')