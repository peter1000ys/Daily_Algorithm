import sys
input = sys.stdin.readline
def back(x, path, used):
    global ans
    global cnt
    if x == len(arr):
        cnt += 1
        if cnt == stop:
            for n in path:
                ans += n
        return
    for i in range(len(arr)):
        if i not in used:
            back(x+1, path + [arr[i]], used + [i])


while True:
    values = input().rstrip().split()
    if len(values) != 2:
        break
    a, stop = values
    arr = list(a)
    stop = int(stop)
    ans = ''
    cnt = 0
    back(0,[], [])
    if cnt < stop:
        ans = 'No permutation'
    print(f'{a} {stop} = {ans}')