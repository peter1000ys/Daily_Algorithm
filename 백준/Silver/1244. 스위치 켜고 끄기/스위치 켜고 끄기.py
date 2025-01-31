import sys
input = sys.stdin.readline

# 남자(1) : 해당 숫자 배수의 스위치만 바꿔 준다
# 여자(2) : 해당 숫자에서 양쪽으로 대칭인 스위치들까지만 바꿔 준다.

# 스위치 수
n = int(input())
# 각 스위치 상태
arr = list(map(int, input().split()))
# 학생 수
students = int(input())
for _ in range(students):
    # 학생의 성별, 학생이 받은 수
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(num, n+1, num):
            arr[i-1] = 1 - arr[i-1]
    elif sex == 2:
        idx = num - 1
        arr[idx] = 1 - arr[idx]
        
        i = 1
        while (idx-i >= 0) and (idx+i < n) and (arr[idx-i] == arr[idx+i]):
            arr[idx-i] = 1 - arr[idx-i]
            arr[idx+i] = 1 - arr[idx+i]
            i += 1
for i in range(0, len(arr), 20):
    print(*arr[i:i+20])


