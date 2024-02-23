"""
N 자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램
2진수 앞자리 0도 반드시 출력

"""

# 테스트 케이스 입력
T = int(input())

# 자리수 N과 N자리 16진수가 주어짐

for tc in range(1, T+1):
    N, hex_num = input().split()

    N = int(N)
    # 16진수를 2진수로 바꾼 결과 값
    bin_num = ''
    for x in hex_num:

        if len(bin(int(x, 16))[2:]) == 3:
            bin_num += '0' + str(bin(int(x, 16))[2:])
        elif len(bin(int(x, 16))[2:]) == 2:
            bin_num += '00' + str(bin(int(x, 16))[2:])
        elif len(bin(int(x, 16))[2:]) == 1:
            bin_num += '000' + str(bin(int(x, 16))[2:])
        else:
            bin_num += str(bin(int(x, 16))[2:])
    print(f'#{tc} {bin_num}')