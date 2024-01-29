import sys

input = sys.stdin.readline

T = 10

#테스트 케이스 동안
for tc in range(1, T+1):
    #입력 받을 총수
    num_of_input = int(input())
    #입력 받은 수들
    arr = list(map(int, input().split()))

    total = 0
    #양 끝은 강변으로 포함시키지 않는다
    for i in range(2, num_of_input-2):
        #기준이 되는 건물에서 양쪽 두칸씩 있는 건물들의 높이를 리스트로 받는다

        num_list = arr[i-2: i+3]
        num_list.remove(arr[i])
        #만약 주변 4개의 건물 중 최댓값이 기준 건물보다 낮으면

        if arr[i] > max(num_list):
            #기준 건물 높이에서 그 최댓값을 빼준만큼 총합에 추가해준다.
            total += arr[i] - max(num_list)
        else:# 기준 건물의 높이가 나머지 4개보다 낮거나 같을 경우는
            #원하는 값에 해당되지 않음으로 넘어간다.
            continue
    print(f'#{tc} {total}')
