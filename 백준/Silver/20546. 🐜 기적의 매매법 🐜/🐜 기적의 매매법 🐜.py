import sys

input = sys.stdin.readline
# 준현이 방법
# 매일 살 수 있으면 최대로 산다
def jun(cash):
    cnt = 0
    for i in range(len(arr)):
        if cash >= arr[i]:
            cnt += cash // arr[i]
            cash = cash % arr[i]
        else:
            continue
    return cash + cnt * arr[-1]

# 성민이 방법
# 1. 모든 거래 주가가 갖고 있는 현금 보다 낮으면 최대한 구매한다
# 2. 3일 연속 상승한다면 전량 매도
# 3. 3일 연속 하락한다면 전량 매수
def seong(cash):
    up, down, cnt = 0, 0, 0
    prev = arr[0]
    for i in range(len(arr)):

        if prev > arr[i]:
            down += 1
            up = 0
        elif prev < arr[i]:
            up += 1
            down = 0
        else:
            up, down = 0, 0
        if up == 3:
            if cash > arr[i]:
                cash += cnt * arr[i]
                cnt = 0
        if down == 3:
            cnt += cash // arr[i]
            cash = cash % arr[i]

        prev = arr[i]

    return cash + cnt * arr[-1]

cash = int(input())
arr = list(map(int, input().split()))
j = jun(cash)
s = seong(cash)
if j > s:
    print('BNP')
elif j < s:
    print('TIMING')
else:
    print('SAMESAME')
