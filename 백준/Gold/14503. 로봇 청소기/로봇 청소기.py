
#     위 왼쪽 아래 오른쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def is_valid(a, b):
    if 0 <= a < n and 0 <= b < m:
        return True
    return False

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

# 주변 4칸 중 청소되지 않은 빈칸이 없고 뒤가 벽일 경우 작동 중지
cnt = 0
cleaned = [[0] * m for _ in range(n)]

if room[r][c] == 0:
    cleaned[r][c] = 1
    cnt = 1
temp = False
while True:
    temp = False
    # 4 방향 중 청소가 안된 곳이 있는 경우
    for _ in range(4):
        d -= 1
        if d < 0:
            d = 3
        nr, nc = r + dr[d], c + dc[d]
        if is_valid(nr, nc) and room[nr][nc] == 0 and cleaned[nr][nc] == 0:
            cleaned[nr][nc] = 1
            cnt += 1
            r, c = nr, nc
            temp = True
            break



    if temp == False:
        dir = d + 2
        if dir > 3:
            dir -= 4
        nr, nc = r + dr[dir], c + dc[dir]
        if is_valid(nr, nc) and room[nr][nc] == 0:
            r, c = nr, nc
        elif room[nr][nc] == 1:
            break

print(cnt)