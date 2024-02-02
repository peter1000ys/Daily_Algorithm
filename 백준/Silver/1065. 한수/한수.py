import sys

input = sys.stdin.readline
# 한수 : 수의 각 자릿수끼리의 차가 같은 등차수열이면 한수
# 1~99까지는 모두 한수
N = int(input())
cnt = 0  # 한수를 세줄 카운트
for i in range(1, N + 1):
    a = list(str(i))  # 숫자를 한번 문자열로 변환시키고 리스트로 받아 각 자릿수를 나눠서 저장한다
    temp = False
    if len(a) > 2:
        for j in range(len(a) - 1, 1, -1):
            if int(a[j]) - int(a[j - 1]) == int(a[j - 1]) - int(a[j - 2]):
                temp = True  # 등차 수열이면 조건을 만족하므로 한수이다
            else:
                temp = False
        if temp:  # 조건을 만족했다면 한수이므로 카운트가 올라간다
            cnt += 1
    else:  # 1~99의 경우 한수이므로 카운트를 세준다
        cnt += 1

print(cnt)
