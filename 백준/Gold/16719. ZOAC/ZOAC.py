import sys
from collections import deque

input = sys.stdin.readline

def solution(words, start):
    global ans

    if words == '':
        return

    min_word = min(words)
    index_min = words.index(min_word)
    ans[start + index_min] = min_word
    print(''.join(ans))

    solution(words[index_min+1:], start + index_min + 1)
    solution(words[:index_min], start)


alpha = input().rstrip()

ans = [''] * len(alpha)
solution(alpha, 0)
