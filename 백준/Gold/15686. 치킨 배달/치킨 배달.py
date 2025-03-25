import sys

input = sys.stdin.readline

def chicken_delivery(start, final):

    if len(final) == M:
        global min_distance
        distance = 0
        for k in range(len(house)):
            h_dist = 10000000
            r1, c1 = house[k]
            for t in final:
                r2, c2 = chicken[t]
                dist = abs(r1-r2) + abs(c1-c2)
                h_dist = min(dist, h_dist)
            distance += h_dist
        min_distance = min(min_distance, distance)
        return

    for e in range(start, len(chicken)):
        if e not in final:
            chicken_delivery(e,final+[e])



N, M = map(int, input().split())

town_map = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
min_distance = 10000000
for i in range(N):
    for j in range(N):
        if town_map[i][j] == 1:
            house.append((i,j))
        elif town_map[i][j] == 2:
            chicken.append((i,j))

chicken_delivery( 0, [])

print(min_distance)