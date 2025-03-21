import sys

input = sys.stdin.readline


S = input().rstrip()

tag = False

ans = ''
word = ''

for i in S:
    if i == '<':
        tag = True
        ans += word[::-1]
        word = i

    elif i == '>':
        tag = False
        word += i
        ans += word
        word = ''

    elif i == ' ':
        if tag:
            word += i
        else:
            ans += word[::-1]
            ans += i
            word = ''
    else:
        word += i

ans += word[::-1]

print(ans)

