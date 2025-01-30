import sys

input = sys.stdin.readline

def back(x, complete, limit, used):

    if x == limit:
        print(complete)
        return

    prev = 0
    for i in range(limit):
        if i not in used and text[i] != prev:
            prev = text[i]
            back(x+1, complete + text[i], limit, used + [i])


n = int(input())
for _ in range(n):

    text = list(input().rstrip())
    text.sort()
    back(0, '', len(text), [])

