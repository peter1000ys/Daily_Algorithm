import sys
input = sys.stdin.readline



for _ in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, input().rstrip().split())

    if a1 < a2 or b1 < b2 or b3 < b0 or a3 < a0:
        print('d')
    elif (a1 == a2 and b1 == b2) or (a1 == a2 and b0 == b3) or (a0 == a3 and b1 == b2) or (a0 == a3 and b0 == b3):
        print('c')
    elif (a1 == a2 and b1 != b2) or (a1 != a2 and b1 == b2) or (b0 == b3 and a0 != a3) or (a0 == a3 and b0 != b3):
        print('b')
    else:
        print('a')

