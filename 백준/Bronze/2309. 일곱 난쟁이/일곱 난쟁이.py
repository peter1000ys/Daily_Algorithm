arr = []
for _ in range(9):
    a = int(input())
    arr.append(a)

for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            q, w = arr[i], arr[j]
            arr.remove(q)
            arr.remove(w)
            arr.sort()
            print(*arr, sep='\n')
            exit()
