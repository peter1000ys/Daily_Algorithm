import sys
input = sys.stdin.readline

N, M = map(int, input().split())

package_cost = []
single_cost = []

for _ in range(M):
    p, s = map(int, input().split())
    package_cost.append(p)
    single_cost.append(s)

min_package = min(package_cost)
total = 0

while N > 0:
    if N >= 6:
        min_single = min(single_cost) * 6
        N -= 6
    else:
        min_single = min(single_cost) * N
        N -= N

    if min_single < min_package:
        total += min_single
    else:
        total += min_package

print(total)