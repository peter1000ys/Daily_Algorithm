import sys

input = sys.stdin.readline
# N : 지방 개수
N = int(input())
# 각 지방 별 요청 예산
arr = list(map(int, input().split()))
# 전체 국가 예산
M = int(input())
# 이진 검색할 범위 설정
start = 1
end = max(arr)

while start <= end:
    # 상한액 : mid
    mid = (start + end) // 2
    cal_sum = 0

    for i in arr:
        # 상한액보다 요청 예산이 적은 경우
        # 해당 요청 예산을 더해줌
        if i < mid:
            cal_sum += i
        # 상한액보다 요청 예산이 큰 경우
        # 상한액을 더해줌
        else:
            cal_sum += mid
    # 만약 지급할 총액이 전체 예산보다 작을 경우
    # 시작점을 상한액 + 1로 설정
    if cal_sum <= M:
        start = mid + 1
    # 만약 지급할 총액이 전체 예산보다 클 경우
    # 시작점을 상한액 - 1로 설정
    else:
        end = mid - 1
print(end)
