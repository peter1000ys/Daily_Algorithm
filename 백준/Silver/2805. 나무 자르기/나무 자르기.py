import sys

input = sys.stdin.readline

# N : 나무의 수, M : 갖고 돌아갈 나무의 수
N, M = map(int, input().split())
# N개 나무의 각 높이
arr = list(map(int, input().split()))

# 이진 검색할 범위 설정
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    sliced_sum = 0

    for i in arr:
        # 잘리는 나무의 길이 합(갖고 갈 나무의 합)을 구한다
        if i >= mid:
            sliced_sum += i - mid
    # 만약 갖고 갈 나무의 길이가 M보다 클 경우 잘라낸 길이가 짧았던 것
    # 이진 탐색 범위의 시작점을 중간지점 + 1로 설정
    if sliced_sum >= M:
        start = mid + 1
    # 만약 갖고 갈 나무의 길이가 M보다 작을 경우 잘라낸 길이가 길았던 것
    # 이진 탐색 범위의 끝점을 중간지점 - 1로 설정
    else:
        end = mid - 1
# 반복이 종료되는 경우가 end < start 이므로
# 마지막 검사에서 가져갈 나무 길이가 목표한 길이 보다 작은 값이 나와
# 거기보다 더 큰 가장 M에 근접한 경우의 H 길이(H의 최댓값)를 출력
print(end)

