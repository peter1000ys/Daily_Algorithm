
n = int(input())
arr = list(input())
sentence = ''
for i in range(n):
    if sentence:
        if arr[i] == 'L':
            if sentence[-1] == 'S':
                sentence += '*L'
            else:
                if sentence[-2] != 'L':
                    sentence += 'L'
                else:
                    sentence += '*L'
        elif arr[i] == 'S':
            sentence += '*S'
        if i == n-1:
            sentence += '*'
    else:
        sentence += '*' + arr[i]
res = sentence.count('*')
if res >= n:
    print(n)
else:
    print(res)