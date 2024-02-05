import sys

input = sys.stdin.readline
# N : 나무 개수, M : 갖고 갈 나무 총 길이
N, M = map(int, input().split())
# trees : N 개의 나무들 각각의 높이
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:

    height = (start + end) // 2  # 시작점과 끝점 중간값을 자를 높이 설정

    tree_sum = 0  # 갖고 갈 나무 길이

    for tree in trees:
        if height < tree:  # 자를 높이가 나무 높이보다 짧은 경우
            tree_sum += tree - height  # 자른 길이를 갖고 갈 나무에 더해줌
        else:
            continue
    if tree_sum >= M:  # 만약 갖고 갈 나무가 원하던 것보다 많이 나오면
        start = height + 1  # 높이 설정이 짧았던 것으로 시작점을 바꿔준다
    else:  # 갖고 갈 나무가 원하던 것보다 적을 경우
        end = height - 1  # 자를 높이 설정이 높았던 것임으로 끝점을 바꿔준다

print(end)
