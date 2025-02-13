import sys

input = sys.stdin.readline

def find(idx, text):

    global ans

    if len(text) == 0:
        return

    min_text = min(text)
    idx_min = text.index(min_text)
    ans[idx+idx_min] = min_text
    print(''.join(ans))

    find(idx+idx_min+1, text[idx_min+1:])
    find(idx, text[:idx_min])

word = input().rstrip()
ans = [''] * len(word)
find(0, word)

