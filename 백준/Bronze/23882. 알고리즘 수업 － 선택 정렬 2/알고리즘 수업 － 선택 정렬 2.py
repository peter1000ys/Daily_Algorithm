import sys

input = sys.stdin.readline
# 배열 A의 크기 N, 교환 횟수 K
N, K = map(int, input().split())
# 배열 A
A = list(map(int, input().split()))
cnt = 0
# 역순으로 비교하는 선택 정렬로 i는 N-1부터 시작해서 0까지 
for i in range(N - 1, -1, -1):
    max_idx = i
    # i를 제외한 i-1부터 0까지
    for j in range(i - 1, -1, -1):
        # 만약 정해놓은 최댓값보다 큰 값이 존재하면 바꿔 준다
        if A[j] > A[max_idx]:
            max_idx = j

    a = A[:]  # 정렬이 몇번 교환 했는지 알기 위해 얕은 복사로 바뀌기 전 상태 저장
    A[max_idx], A[i] = A[i], A[max_idx]
    if A != a:  # 교환이 일어 났다면 카운트 + 1
        cnt += 1
    if K == cnt:  # K랑 카운트가 같아지는 순간의 정렬 상태를 출력한다
        print(*A, sep=' ')
        break
if cnt < K:  # 교환이 설정해 놓은 K값 보다 적게 일어 났으면 -1 출력
    print(-1)
