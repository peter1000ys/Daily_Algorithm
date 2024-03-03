
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    deq = deque(arr)
    all_num = []
    while True:
        new = []
        cnt = 0
        for i in range(0,N,N//4):
            arr_ = list(deq)
            a = ''.join(arr_[i:i+N//4])
            new.append(a)
        for i in new:
            if i in all_num:
                cnt += 1
            else:
                all_num.append(i)
        if cnt == len(new):
            break
        deq.rotate(1)

    all_num.sort(key=lambda x: int(x, 16), reverse=True)

    print(f'#{tc} {int(all_num[K-1],16)}')