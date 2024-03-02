T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    people = 0
    hired = 0
    for i in range(len(arr)):
        if arr[i] != '0':
            if people + hired < i:
                hired += i - (people + hired)
            people += int(arr[i])
    print(f'#{tc} {hired}')