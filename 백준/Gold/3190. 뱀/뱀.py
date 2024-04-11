from collections import deque

# 전체 칸의 한변 길이
n = int(input())
# 사과의 개수
k = int(input())
# 사과의 위치
apples = [tuple(map(int, input().split())) for _ in range(k)]
# 뱀의 방향 전환 횟수
l = int(input())
tlst = [list(input().split()) for _ in range(l)]
# 뱀의 위치는 (0, 0), 뱀의 길이는 1, 일단은 오른쪽으로 이동한다
r, c = 1, 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
cnt = sec = d = 0
snake_len = 1
snake = deque()
snake.append((1, 1))
while True:
    nr, nc = r + dr[d], c + dc[d]
    if nr < 1 or nr > n or nc < 1 or nc > n or (nr, nc) in snake:
        break
    if (nr, nc) in apples:
        apples.pop(apples.index((nr,nc)))
        snake_len += 1
    snake.append((nr, nc))
    r, c = nr, nc
    sec += 1
    if cnt < len(tlst) and sec == int(tlst[cnt][0]):
        if tlst[cnt][1] == 'D':
            d += 1
            if d == 4:
                d = 0
        elif tlst[cnt][1] == 'L':
            d -= 1
            if d == -1:
                d = 3
        cnt += 1
    while len(snake) != snake_len:
        if len(snake) > snake_len:
            snake.popleft()


print(sec+1)