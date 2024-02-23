"""
NxN 배열 안 영역에 존재하는 파리의 개체 수 표시
스프레이 노즐 형태는  + 또는 x
M은 스프레이 분사 세기
잡을 수 있는 최대 파리 수 출력

"""
#     상 하 좌 우
dr1 = [-1, 1, 0, 0]
dc1 = [0, 0, -1, 1]
# 대각선
dr2 = [-1, 1, 1, -1]
dc2 = [1, 1, -1, -1]

# 테스트 케이스 수 입력
T = int(input())

for tc in range(1, T + 1):
    board = []
    N, M = map(int, input().split())
    # NxN 판 입력
    for _ in range(N):
        board.append(list(map(int, input().split())))
    sum_flies = []
    for r in range(N):
        for c in range(N):
            ans = board[r][c]
            ans1 = board[r][c]
            for x in range(1,M):
                for i in range(4):

                    row1 = r + dr1[i] * x
                    col1 = c + dc1[i] * x
                    row2 = r + dr2[i] * x
                    col2 = c + dc2[i] * x
                    if 0 <= row1 < N and 0 <= col1 < N:
                        ans += board[row1][col1]
                    if 0 <= row2 < N and 0 <= col2 < N:
                        ans1 += board[row2][col2]
                    else:
                        continue
            sum_flies.append(ans)
            sum_flies.append(ans1)
    print(f'#{tc} {max(sum_flies)}')
