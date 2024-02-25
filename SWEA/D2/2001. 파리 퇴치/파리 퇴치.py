"""
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 출력

입력 :
1. 테스트 케이스 수
2. N, M
3. N 줄을 거쳐 NxN 배열이 주어짐

출력:
# tc 정답을 출력

"""
# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    # NxN 배열을 입력 받음
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    all_sum = []
    # 판 안에서 존재할 수 있는 모든 MxM판 내의 모든 죽은 파리 개수
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_flies = 0
            for r in range(M):
                for c in range(M):
                    sum_flies += board[i + r][j + c]
            all_sum.append(sum_flies)
    print(f'#{tc} {max(all_sum)}')