import sys

input = sys.stdin.readline

def theSeven(start, picked):
    if len(picked) == 7:
        if sum(picked) == 100:
            print(*picked, sep='\n')
        return

    for i in range(start, len(dwarfs)):
        if dwarfs[i] not in picked:
            theSeven(i, picked+[dwarfs[i]])


dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

theSeven(0, [])