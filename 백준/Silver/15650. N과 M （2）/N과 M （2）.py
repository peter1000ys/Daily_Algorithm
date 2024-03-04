# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다
def NnM(x, start, arr):
    if x == m:
        print(*arr, sep=' ')
        return

    for i in range(start, n+1):
        NnM(x+1, i + 1, arr + [i])


n, m = map(int, input().split())
NnM(0, 1, [])