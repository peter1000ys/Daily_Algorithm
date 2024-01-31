S, M = map(int, input().split())
"""
~ : NOT 연산자로 모든 비트를 반전시키는 비트
& ~을 이용하여 앞 피연산자는 뒤 피연산자의 부분집합이거나 공집합인지 확인 할 수 있다
쉽게 말해 ahri의 비트 연산자를 빼줘서 결과가 0이 안 나오면 남는 값이 생긴다는 것이다.

예)
S = 512
ahri = 11111111
    1000000000
   -1111111111
   ------------
   0000000000
하지만 S가 1024 이상이면 남는 값이 생긴다
    10000000000
   -01111111111
   ------------
   1000000000

"""
# 아리가 가진 돈의 총합
ahri_total = 1023

if S <= ahri_total:
    print("No thanks")
else:
    remain = S - ahri_total
    if remain & ~(M) == 0:
        print("Thanks")

    else:
        print("Impossible")
