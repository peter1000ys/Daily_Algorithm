import sys
from copy import deepcopy
input = sys.stdin.readline


def check_up(row):
    for j in range(k-1):
        if row[j] == '-':
            start[j], start[j+1] = start[j+1], start[j]



def check_down(row):
    for j in range(k-1):
        if row[j] == '-':
            end[j], end[j + 1] = end[j + 1], end[j]



k = int(input())
n = int(input())
end = list(input().rstrip())
start = sorted(end)
ladders = [list(input().rstrip()) for _ in range(n)]



for i in range(n):
    if '?' in ladders[i]:
        break

    else:
        check_up(ladders[i])

for i in range(n-1, -1, -1):
    if '?' in ladders[i]:
        break

    else:
        check_down(ladders[i])

result = []

for i in range(k-1):
    if start[i] == end[i]:
        result.append('*')

    elif start[i] == end[i+1]:
        result.append('-')

    elif i != 0 and start[i] == end[i-1]:
        result.append('*')

    else:
        result = ['x' for _ in range(k-1)]
        break

print(''.join(result))