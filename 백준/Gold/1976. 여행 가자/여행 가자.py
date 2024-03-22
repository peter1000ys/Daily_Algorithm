def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


# 도시의 수
n = int(input())

# 여행 계획에 속한 도시들 수
m = int(input())
parents = [i for i in range(n)]
# 연결 되어 있는 연결 행렬을 입력 받음
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_set(i, j)

arr = list(map(int, input().split()))
temp = True
prev = find_set(arr[0] - 1)
for i in range(1, m):
    if prev != find_set(arr[i] - 1):
        temp = False
if temp:
    print('YES')
else:
    print('NO')

