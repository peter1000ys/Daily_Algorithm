# 이러니까 잠을 못자지
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = []
    a = 1
    new = 0
    while len(arr) < 10:
        new = n * a
        for i in list(str(new)):
            if i not in arr:
                arr.append(i)
        a += 1
    print(f'#{tc} {new}')