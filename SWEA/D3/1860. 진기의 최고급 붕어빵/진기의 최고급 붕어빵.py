"""
진기는 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
0초 이후에 손님들이 언제 도착하는지 주어지면,
모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성

입력 :
테스트 케이스의 수 T
세 자연수 N, M, K(1 ≤ N, M, K ≤ 100)
N개의 정수가 공백으로 구분되어 주어짐
각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타낸다. 각 수는 0이상 11,111이하이다.

출력 : 모든 손님들에 대해 기다리는 시간 없이 붕어빵 제공 시 "Possible"
아니라면 "Impossible"


"""


def start():
    sold_bread = 0
    for person in customers:
        made_bread = (person // M) * K
        sold_bread += 1
        remain = made_bread - sold_bread

        if remain < 0:
            return 'Impossible'
    return 'Possible'


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    customers = list(map(int, input().split()))
    customers.sort()

    print(f'#{tc} {start()}')
