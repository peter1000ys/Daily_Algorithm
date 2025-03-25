import sys

input = sys.stdin.readline

# n장이 카드 중 3장을 골라야 한다
# 3장의 합이 M을 넘지 않고 최대한 가깝게 만들어야 한다.
def blackJack(start, picked):

    global sum_max

    if len(picked) == 3:
        if sum(picked) <= M:
            sum_max = max(sum_max, sum(picked))
        return

    for i in range(start, N):
        if cards[i] not in picked:
            blackJack(i, picked+[cards[i]])


# N 장의 카드, 숫자 M
N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum_max = 0
blackJack(0, [])
print(sum_max)

