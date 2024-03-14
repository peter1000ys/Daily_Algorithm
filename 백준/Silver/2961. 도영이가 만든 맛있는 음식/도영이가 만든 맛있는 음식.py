import sys
input = sys.stdin.readline

def cook(x, start, sour, bitter):
    global min_
    if x > 0 and abs(sour - bitter) < min_:
        min_ = abs(sour - bitter)

    if x == n:

        return

    for i in range(start, n):
        s1, b1 = lst[i]
        cook(x+1, i+1,  sour*s1, bitter+b1)


n = int(input())
lst = []

min_ = 1000000000
for _ in range(n):
    s, b = map(int, input().split())
    lst.append((s,b))
cook(0,0,1,0)
print(min_)