# 화살표 방향을 거슬러 올라갈 수 없는 DFS 문제
# 출발점 0, 도착점 99
# 입력 : 각 테스트 케이스의 간선의 총 개수가 주어짐
# 그리고 순서쌍들도 주어진다
# 출력 : 도착 여부를 출력

def dfs(T):
    visited[T] = 1
    for node in adjl[T]:
        if visited[node] == 0:
            dfs(node)


for tc in range(1, 11):
    t, E = map(int, input().split())
    visited = [0] * 101
    adjl = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    for i in range(len(arr)//2):
        a, b = arr[i * 2], arr[i * 2 + 1]
        adjl[a].append(b)
    dfs(0)
    print(f'#{tc}', end=' ')
    if visited[99]:
        print(1)
    else:
        print(0)