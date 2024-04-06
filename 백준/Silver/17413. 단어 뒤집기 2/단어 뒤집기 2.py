sentence = list(input())
result = ''
stack = []
temp = False
for i in range(len(sentence)):
    if sentence[i] == ' ' and temp == False:
        while stack:
            result += stack.pop()
        result += sentence[i]
    elif i == len(sentence)-1 and temp == False:
        result += sentence[i]
        while stack:
            result += stack.pop()
    elif sentence[i] == '<':
        while stack:
            result += stack.pop()
        result += sentence[i]
        temp = True
    elif sentence[i] == '>':
        result += sentence[i]
        temp = False
    else:
        if temp:
            result += sentence[i]
        else:
            stack.append(sentence[i])

print(result)

