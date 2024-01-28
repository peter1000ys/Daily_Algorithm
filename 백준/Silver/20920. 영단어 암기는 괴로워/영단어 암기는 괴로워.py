import sys

input = sys.stdin.readline
#N = 나오는 영어 단어 개수, M은 최소 단어의 길이
N, M = map(int, input().split())

#단어들을 담아둘 딕셔너리 생성
memorize = {}

for i in range(N):
    words = input().rstrip()

    if len(words) >= M:     #정한 최소 단어 길이랑 같거나 크면
        if words not in memorize:   #해당 단어가 딕셔너리에 없으면 값은 1
            memorize[words] =1
        else:   #있다면 값에 1을 더해준다
            memorize[words] += 1

"""
    단어장에 단어들이 정렬되는 조건으로
    1. 자주 나오는 단어일수록 앞에 배치한다.
    2. 해당 단어의 길이가 길수록 앞에 배치한다.
    3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
    를 순서대로 맞게 정렬 시켜준다
"""
memorize_sorted = sorted(memorize, key = lambda x: (-memorize[x], -len(x), x))

print(*memorize_sorted, sep='\n')