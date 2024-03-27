import sys
input = sys.stdin.readline
n = int(input())
f1 = [0] * (n+1)
cnt = 0
def fib(n):
    global cnt
    if n == 1 or n == 2:
        cnt += 1
        return 1
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    cnt = 0
    f1[1] = 1
    f1[2] = 1
    for i in range(3, n+1):
        cnt += 1
        f1[i] = f1[i-1] + f1[i-2]
    return cnt
fib(n)
print(cnt, fibonacci(n))