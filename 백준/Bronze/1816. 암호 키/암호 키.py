import sys

# S의 모든 소인수가 106보다 크다면 그 수는 적절한 암호 키

input = sys.stdin.readline
test = int(input())

for T in range(test):
    secretCode = int(input())
    for i in range(2, 10**6 + 1):
        if secretCode % i == 0:
            print("NO")
            break
        if i == 10**6:
            print("YES")