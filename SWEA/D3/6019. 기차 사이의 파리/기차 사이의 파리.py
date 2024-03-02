T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    f = D / (A + B) * F
    print(f'#{tc} {f}')