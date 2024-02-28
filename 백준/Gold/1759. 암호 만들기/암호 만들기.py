L, C = map(int, input().split())
arr = input().split()
arr.sort()

vowels = ['a', 'e', 'i', 'o', 'u']


def check(arr):
    cnt = 0
    for i in arr:
        if i in vowels:
            cnt += 1
    if cnt > 0 and L - cnt > 1:
        return True
    return False


def f(x, a):
    if x == L:
        if check(a):
            print(''.join(a))
        return

    for i in range(len(arr)):
        if a[-1] < arr[i]:
            a.append(arr[i])
            f(x+1, a)
            a.pop()


for x in range(C-L+1):
    a = [arr[x]]
    f(1, a)
