import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

switch = 0
# 제일 큰 수를 뒤로 보내서 마지막 인덱스에 위치시키고 그 인덱스를 제외하고 반복하는 버블 정렬
for i in range(N - 1, 0, -1):  # 마지막 인덱스
    for j in range(i):  # 가장 왼쪽 인덱스 부터 i 인덱스까지 비교 및 교환
        if arr[j] > arr[j + 1]:
            switch += 1  # 비교 과정에서 오른쪽 값이 왼쪽 값보다 작으면 교환이 일어남
            arr[j + 1], arr[j] = arr[j], arr[j + 1]

            if switch == K:  # K번째 교환에서 교환한 값 2개를 오름차순으로 출력
                print(arr[j], arr[j + 1])

if switch < K:
    # 만약 교환한 횟수가 K보다 적으면 -1 출력
    print(-1)
