def cal(lst):
    total = 0
    for hi, hj in ones:
        min_ = 1000000
        for i in lst:
            ci, cj = chickens[i]
            min_ = min(min_, abs(hi-ci) + abs(hj -cj))
        total += min_
    return total

def back(x, start, path):
    global min_v
    if x == m:
        min_v = min(min_v, cal(path))
        return

    for i in range(start, len(chickens)):
        back(x+1, i+1, path + [i])



def find(x):
    lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == x:
                lst.append((i, j))
    return lst


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
min_v = 1000000
ones = find(1)
chickens = find(2)
back(0, 0, [])
print(min_v)