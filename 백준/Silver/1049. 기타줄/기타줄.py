import sys
input = sys.stdin.readline
"""
결국 패키지 가격 중 가장 싼 값과 낱개의 가격 중 가장 싼 값을 가져 와서
상황에 따라 비교하여 최소의 경우를 찾는 문제

N이 6보다 큰 경우
낱개의 최솟값 * 6 과 패키지 최솟값을 비교하여 더 낮은 가격을 선택

N이 6보다 작은 경우
낱개의 최솟값 * N 과 패키지 최솟값을 비교하여 더 낮은 가격을 선택
"""
N, M = map(int, input().split())

package = []
one = []

for _ in range(M):
    p, o = map(int, input().split())
    package.append(p)
    one.append(o)

min_package = min(package)


total = 0

while N > 0:
    if N >= 6:
        min_one = min(one) * 6
        N -= 6
    else:
        min_one = min(one) * N
        N -= N

    if min_one < min_package:
        total += min_one
    else:
        total += min_package

print(total)