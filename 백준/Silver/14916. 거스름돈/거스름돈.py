import sys
input = sys.stdin.readline

N = int(input())
coin = 0
while N > 0:
    if N >= 5:
        coin += N // 5
        N %= 5
        if N % 2:
            N += 5
            coin += (N // 2) - 1
            N %= 2
            break

    elif N % 2 == 0:
        coin += N // 2
        N %= 2

    else:
        coin = -1
        break

print(coin)

