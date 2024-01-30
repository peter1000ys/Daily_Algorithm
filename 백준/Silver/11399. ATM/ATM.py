import sys

input = sys.stdin.readline

N = int(input())
# 각각 이용 하는데 걸리는 시간 입력
time_needed = list(map(int, input().split()))

# 이용 하는데 걸리는 시간 오름차 순으로 정렬
time_needed = sorted(time_needed)

# 다음 사람은 전 사람이 쓴 만큼 기다린 다음에 사용 가능
for i in range(1, N):
    time_needed[i] += time_needed[i - 1]
# 필요한 시간의 합의 최솟값
print(sum(time_needed))
