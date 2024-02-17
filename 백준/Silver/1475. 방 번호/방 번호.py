import sys
input = sys.stdin.readline
cnt = [0]*10
N = list(map(int, str(input().rstrip())))



for x in N:

    if x == 6 or x == 9:
        if cnt[6] <= cnt[9]:
            cnt[6] += 1
        else:
            cnt[9] += 1
    else:
        cnt[x] += 1
print(max(cnt))