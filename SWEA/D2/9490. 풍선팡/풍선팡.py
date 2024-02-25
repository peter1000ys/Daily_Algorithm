"""
풍선 N x M 구조
풍선을 터트리면 안에 있는 꽃가루 개수 만큼 상하좌우 풍선이 추가로 터짐
한개의 풍선을 터트렸을 때 날릴 수 있는 꽃가루 합 중 최댓값

입력 :
1. 테스트 케이스
2. N, M
3. 각 풍선마다 들어 있는 꽃가루 수

출력 :
# 테스트 케이스 꽃가루 최대 개수
"""
#     상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 테스트 케이스 수
T = int(input())
for tc in range(1, T+1):
    # 풍선 판 입력
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 터지는 꽃가루 개수를 모아 놓을 리스트
    all_sum = []
    for r in range(N):
        for c in range(M):
            sum_flower = board[r][c]
            # 터진 풍선의 꽃가루 개수만큼 상하좌우로 풍선이 터짐
            for i in range(1, board[r][c] + 1):
                for d in range(4):
                    nr, nc = r + dr[d] * i, c + dc[d] * i
                    # 범위를 벗어나지 않는 값, 즉 풍선이 있으면 그 값을 더해준다
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_flower += board[nr][nc]
            # 구한 꽃가루 수 추가
            all_sum.append(sum_flower)
    print(f'#{tc} {max(all_sum)}')