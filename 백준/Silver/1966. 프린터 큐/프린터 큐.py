import sys

input = sys.stdin.readline

test_case = int(input())

#입력 받은 테스트 케이스 동안
for _ in range(test_case):
    cnt = 0
    N, M = map(int,input().split())
    #N은 총 구성 요소 수, M은 현재 내가 언제 빠지는지 알고 싶은 원소 위치
    importance = list(map(int, input().split()))
    #중요도 입력 받음

    while importance:   #중요도가 비어있지 않는 이상
        max_num = max(importance)
        #현재 최댓수를 뽑아줌
        front = importance.pop(0)
        #큐이므로 가장 앞에 있는 수 뽑아줌
        M -= 1
        #앞에 값을 뽑았으니 원하는 값의 위치는 한칸 당겨진다

        if front == max_num:    #최댓값과 뽑은 값이 일치할 경우
            cnt += 1    #pop이 되었으므로 카운트가 올라가고
            if M < 0:   #만약 위치가 -1이면 빠져 나간게 내가 원하는 수이므로
                print(cnt)  #출력에 대한 카운트를 출력
                break   #while문 종료
        else:
            importance.append(front)
            #중요도가 최댓값이 아니면 다시 큐의 맨 뒤에 삽입해준다
            if M < 0:
                #만약 방금 뽑았던 수가 내가 원하는 수였으면
                M = len(importance) - 1
                #위치가 큐의 가장 뒤로 바꿔었음으로 값을 바꿔준다