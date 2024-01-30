import sys

input = sys.stdin.readline

N = int(input())

times = [[0, 0] for _ in range(N)]

for x in range(N):
    a, b = map(int, input().split())
    times[x][0] = a
    times[x][1] = b

times.sort(key = lambda x: (x[1], x[0]))

end_time = times[0][1]
count = 1

for i in range(1, N):
    if times[i][0] >= end_time:
        count += 1
        end_time = times[i][1]


print(count)
