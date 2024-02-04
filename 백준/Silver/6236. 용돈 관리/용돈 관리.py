import sys

input = sys.stdin.readline
# N : 돈을 사용할 일수
# M : 통장에서 돈을 인출할 횟수
N, M = map(int, input().split())
# 7일동안 각 날마다 사용할 금액
arr = [int(input()) for _ in range(N)]

# 만약 인출할 금액이 하루 사용량보다 적으면 
# 인출을 아무리 해도 그 날 돈은 사용을 못한다
# 조건에서 무조건 남은 금액 모두를 입금하고
# k원을 인출한다고 했기 때문
start = max(arr)

end = sum(arr)

while start <= end:

    k = (start + end) // 2
    # 현재 한번 인출한 상황으로 1로 시작한다
    cnt = 1
    remain = k

    for i in arr:
        # 만약 남아 있는 금액이 해당 날 사용량보다 적으면
        # 나머지를 입금하고 새로 K원 인출
        # 인출이 한번 이루어졌으므로 카운트 +1
        if remain < i:
            remain = k - i
            cnt += 1
        else:
            remain -= i
    
    # 카운트가 원하던 횟수보다 많으면
    # k 금액이 적어서 여러번 인출한 상황으로
    # k 금액을 늘린다
    if cnt > M:
        start = k + 1
    # 카운트가 원하던 횟수보다 적으면
    # k 금액이 많아서 남는 금액이 많아 
    # M보다 더 적게 인출한 상황으로
    # k 금액을 줄인다
    else:
        end = k - 1
# 인출 금액 K의 최솟값을 출력
print(start)
