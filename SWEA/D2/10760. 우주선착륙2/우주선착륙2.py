"""
우주선 착륙 문제
착륙 지점보다 낮은 구역의 사진을 찍을 수 있다
예비 착륙 후보지를 찾는 문제
예비 후보지 : 후보지 주변 8칸 중에서
사진을 찍을 수 있는 방향이 4방향 이상인 지점으로 정함
조건을 만족하는 예비 후보지 구역 개수를 출력
"""
#     상 하 좌 우
dr1 = [-1, 1, 0, 0]
dc1 = [0, 0, -1, 1]
# 대각선
dr2 = [-1, 1, 1, -1]
dc2 = [1, 1, -1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = []
    for row in range(N):
        arr = list(map(int, input().split()))
        board.append(arr)
    possible_standard = 0
    for x in range(N):
        for y in range(M):
            standard = board[x][y]
            cnt = 0
            for i in range(4):

                row1 = x + dr1[i]
                col1 = y + dc1[i]
                row2 = x + dr2[i]
                col2 = y + dc2[i]
                if 0 <= row1 < N and 0 <= col1 < M:
                    if board[row1][col1] < standard:
                        cnt += 1

                if 0 <= row2 < N and 0 <= col2 < M:
                    if board[row2][col2] < standard:
                        cnt += 1

            if cnt >= 4:
                possible_standard += 1
    print(f'#{tc} {possible_standard}')
