import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


def bubblesort(arr, arr2):
    for i in range(N - 1, 0, -1):  # 마지막 인덱스
        for j in range(i):  # 가장 왼쪽 인덱스 부터 i 인덱스까지 비교 및 교환
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                if arr[j] == arr2[j]:
                    if arr == arr2:
                        print(1)
                        sys.exit(0)
    print(0)


if arr == arr2:
    print(1)
    sys.exit(0)
else:
    bubblesort(arr, arr2)
