import sys

input = sys.stdin.readline

n = int(input())

carry = []

for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        carry.append(i)
        n = int(n/i)
if n != 1:
    carry.append(n)

print(len(carry))
print(*carry)