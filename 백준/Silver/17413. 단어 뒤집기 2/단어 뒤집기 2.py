import sys
input = sys.stdin.readline

sentence = input().rstrip()
stack = []
arr = []
temp = 0
ans = ''
for i in range(len(sentence)):
    if sentence[i] == '<':
        temp = 1
        arr.append(sentence[i])
        if stack:
            stack.reverse()
            ans += ''.join(stack)
            stack = []

    elif sentence[i] == ' ':
        if temp:
            arr.append(sentence[i])
        else:
            stack.reverse()
            stack.append(sentence[i])
            ans += ''.join(stack)
            stack = []

    else:
        if temp:
            arr.append(sentence[i])
            if sentence[i] == '>':
                temp = 0
                ans += ''.join(arr)
                arr = []


        else:
            stack.append(sentence[i])

    if temp == 0 and i == len(sentence) -1:
        stack.reverse()
        ans += ''.join(stack)
print(ans)



