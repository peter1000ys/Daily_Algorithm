import sys

input = sys.stdin.readline

#N = 듣도 못한 사람 수, M = 보도 못한 사람 수

N, M = map(int, input().split())

#듣도 보도 못한 사람을 교집합으로 구하기 위해 세트로 나눈다

never_heard = set()
never_seen = set()



for i in range(N + M):
    if i < N:   #듣도 못한 사람들 입력
        never_heard.add(input().rstrip())
    else:       #보도 못한 사람들 입력
        never_seen.add(input().rstrip())

#듣보잡 = 듣도 못한 사람들과 보도 못한 사람들의 교집합
never_seen_heard = never_heard & never_seen

#이름 알파벳 순으로 정렬
sorted_never_seen_heard = sorted(never_seen_heard)

#듣보잡 수와 그 명단을 사전 순으로 출력
print(f'{len(never_seen_heard)}')
print(*sorted_never_seen_heard, sep='\n')