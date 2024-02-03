N = int(input())

arr = []
# 정렬하고 싶은 배열을 입력 받는다
for _ in range(N):
    arr.append(int(input()))

arr.sort()
arr.reverse()
print(*arr, sep='\n')

