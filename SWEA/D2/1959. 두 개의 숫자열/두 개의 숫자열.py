T = int(input())
for tc in range(1, T+1):
    numbers = []
    N, M = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if N >= M:
        for i in range(N - M + 1):
            sum_ = 0
            for j in range(M):
                sum_ += arr1[i+j] * arr2[j]
            numbers.append(sum_)
    else:
        for i in range(M-N+1):
            sum_ = 0
            for j in range(N):
                sum_ += arr1[j] * arr2[i+j]
            numbers.append(sum_)
    print(f'#{tc} {max(numbers)}')