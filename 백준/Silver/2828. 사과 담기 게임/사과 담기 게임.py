n, m = map(int, input().split())
j = int(input())
arr = []
l, r = 1, m
ans = 0

for _ in range(j):
    apple = int(input())
    # 사과가 범위 안에 떨어지면 이동 없음
    if l <= apple <= r:
        continue
    # 바구니 보다 왼쪽에 떨어질 경우
    elif l > apple:
        ans += (l - apple)
        r -= (l - apple)
        l = apple
    # 바구니 보다 오른쪽에 떨어질 경우
    else:
        ans += (apple - r)
        l += (apple - r)
        r = apple

print(ans)
