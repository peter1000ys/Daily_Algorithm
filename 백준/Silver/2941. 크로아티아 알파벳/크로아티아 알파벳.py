sentence = list(input())
prev =''
cnt = 0
for i in range(len(sentence)):
    if sentence[i] == 'j' and (prev == 'l' or prev == 'n'):
        prev = sentence[i]

    elif sentence[i] == '-' and (prev == 'c' or prev == 'd'):
        prev = ''
    elif sentence[i] == '=' and (prev == 's' or prev == 'dz' or prev == 'z' or prev == 'c'):
        prev = ''
    elif sentence[i] == 'z' and prev == 'd':
        prev += sentence[i]
    else:
        prev = sentence[i]
        cnt += 1
    if (i+1 == len(sentence) or sentence[i+1] != '=') and prev == 'dz':
        cnt += 1
        prev = ''
        continue
print(cnt)