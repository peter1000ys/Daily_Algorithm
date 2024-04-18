from copy import deepcopy
from collections import deque


def check(qlst):
    for i in range(n):
        for j in range(m):
            if qlst[i][j] == 1:
                return False
    return True


def move(alst):
    alst.pop()
    alst = [[0] * m] + alst

    return alst


def start(lst):
    test = deepcopy(arr)
    cnt = 0
    arc_x = n
    while True:
        kill = set()
        enemy = enemyFind(test)
        for arc_y in lst:
            min_v = 1e9
            ax, ay = 0, 0
            temp = False
            for enemy_x, enemy_y in enemy:

                dist = abs(arc_x - enemy_x) + abs(arc_y - enemy_y)
                if dist <= d:
                    if dist < min_v:
                        ax, ay = enemy_x, enemy_y
                        temp = True
                    min_v = min(min_v, dist)
            if temp:
                kill.add((ax, ay))

        for q1, q2 in kill:
            test[q1][q2] = 0
            cnt += 1

        test = move(test)
        if check(test):
            return cnt


def enemyFind(tlst):
    enemy = []
    for i in range(n):
        for j in range(m):
            if tlst[i][j] == 1:
                enemy.append((i, j))
    enemy.sort(key=lambda x: x[1])
    return enemy


def comp(x, s, path):
    global max_
    if x == 3:
        max_ = max(max_, start(path))
        return

    for i in range(s, m):
        if i not in path:
            comp(x + 1, i + 1, path + [i])


n, m, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_ = 0
comp(0, 0, [])
print(max_)
