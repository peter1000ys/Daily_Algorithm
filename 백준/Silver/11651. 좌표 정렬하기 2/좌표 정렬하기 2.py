import sys

input = sys.stdin.readline

num_list = []

N = int(input())

for i in range(N):
    num_list.append(list(map(int, input().split())))

num_list = sorted(num_list, key=lambda x: (x[1], x[0]))

for j in num_list:
    print(*j)
