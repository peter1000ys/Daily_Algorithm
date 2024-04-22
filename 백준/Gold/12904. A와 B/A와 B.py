import sys
input = sys.stdin.readline
arr_s = list(input().rstrip())
arr_t = list(input().rstrip())
while True:
    if len(arr_s) == len(arr_t):
        if arr_s == arr_t:
            print(1)
            break
        else:
            print(0)
            break

    word = arr_t.pop()
    if word == 'A':
        continue
    elif word =='B':
        arr_t.reverse()

