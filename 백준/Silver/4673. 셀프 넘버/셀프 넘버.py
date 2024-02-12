N = [0 for _ in range(10001)]

for i in range(1, 10001):
    DR = i
    a = i
    while True:
        DR += a % 10
        if a // 10 == 0:
            break
        else:
            a = a // 10
    if DR >= len(N):
        continue
    N[DR] = 1

for i in range(1, len(N)):
    if N[i] == 0:
        print(i)