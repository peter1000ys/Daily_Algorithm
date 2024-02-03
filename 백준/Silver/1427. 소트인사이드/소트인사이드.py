import sys
input = sys.stdin.readline

N = list(input().rstrip())
N = sorted(list(map(int, N)))
N.reverse()
a = ''.join(map(str, N))

print(int(a))

