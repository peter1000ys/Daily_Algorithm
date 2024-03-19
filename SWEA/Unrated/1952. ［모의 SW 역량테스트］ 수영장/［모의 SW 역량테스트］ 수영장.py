def count_money(x, cnt):
    global min_cost
    if cnt >= min_cost:
        return

    if x >= len(calendar):
        min_cost = min(min_cost, cnt)
        return

    if calendar[x]:

        for i in range(2):

            if i == 1:
                count_money(x+3, cnt + money[2])
            else:
                for j in range(2):
                    if j == 0:
                        count_money(x + 1, cnt + money[0] * calendar[x])
                    else:
                        count_money(x + 1, cnt + money[1])
    else:
        count_money(x+1, cnt)


T = int(input())
for tc in range(1, T+1):
    money = list(map(int, input().split()))
    calendar = list(map(int, input().split()))
    min_cost = money[3]
    count_money(0, 0)
    print(f'#{tc} {min_cost}')