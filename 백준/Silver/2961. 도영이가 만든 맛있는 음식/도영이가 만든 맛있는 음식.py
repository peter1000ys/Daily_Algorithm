import sys

input = sys.stdin.readline
# 사용한 재료 신맛의 곱, 쓴맛의 합
def food(arr):
    multiply_S, sum_B = 1, 0
    for i in arr:
        multiply_S *= S[i]
        sum_B += B[i]
    return abs(multiply_S - sum_B)

# 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다
def cook(start, picked):
    global min_res
    if picked:
        min_res = min(food(picked), min_res)

    for i in range(start, N):
        if i not in picked:
            cook(i, picked+[i])




# 재료 N개, 신맛 S, 쓴맛 B
N = int(input())
S, B = [], []
min_res = 1000000000
for _ in range(N):
    s, b = map(int, input().split())
    S.append(s)
    B.append(b)
cook(0,[])
print(min_res)