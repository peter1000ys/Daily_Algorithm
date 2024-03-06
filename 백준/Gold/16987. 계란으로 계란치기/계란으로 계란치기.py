def egg(x, cnt):
    global max_
    # 가지치기
    if cnt + (n-x)*2 <= max_: return
    # 모든 계란 부딪히기 완료
    if x == n:
        # 정답 갱신
        max_ = max(cnt, max_)
        return
    if arr[x][0] <= 0:
        # 현재 계란이 깨진 경우 다음 계란으로 이동
        egg(x + 1, cnt)
    else:
        tmp = False  # 하나도 안 부딪혔을 경우

        # 현재 계란이 안 깨졌을 경우
        for i in range(n):
            if x == i or arr[i][0] <= 0:
                continue
            tmp = True
            arr[x][0] -= arr[i][1]
            arr[i][0] -= arr[x][1]
            egg(x + 1, cnt + int(arr[x][0] <= 0) + int(arr[i][0] <= 0))
            arr[x][0] += arr[i][1]
            arr[i][0] += arr[x][1]
        if tmp == False:
            egg(x + 1, cnt)


n = int(input())
max_ = 0
arr = [list(map(int, input().split())) for i in range(n)]
egg(0, 0)
print(max_)
