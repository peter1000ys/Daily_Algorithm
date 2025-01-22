import sys
input = sys.stdin.readline

N = int(input())
deck = []

for i in range(N):

    n = input().split()
    if n[0] == 'push_front':
        deck.insert(0, n[1])
    elif n[0] == 'push_back':
        deck.append(n[1])
    elif n[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print('-1')
    elif n[0] == 'back':
        if deck:
            print(deck[-1])
        else:
            print('-1')

    elif n[0] == 'size':
        print(len(deck))

    elif n[0] == 'empty':
        if deck:
            print('0')
        else:
            print('1')

    elif n[0] == 'pop_front':
        if deck:
            print(deck.pop(0))
        else:
            print('-1')
    elif n[0] == 'pop_back':
        if deck:
            print(deck.pop(-1))
        else:
            print('-1')

