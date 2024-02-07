import sys
input = sys.stdin.readline
T = int(input())
for tc in range(T):
    sentence = input()
    stack = []
    ans = ''
    for i in range(len(sentence)):
        if sentence[i] == ' ' or i == len(sentence)-1:
            while stack:
                ans += stack.pop()
            ans += ' '
        else:
            stack.append(sentence[i])

    print(ans)