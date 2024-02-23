T = int(input())
secret_code = {'0001101': 0,
               '0011001': 1,
               '0010011': 2,
               '0111101': 3,
               '0100011': 4,
               '0110001': 5,
               '0101111': 6,
               '0111011': 7,
               '0110111': 8,
               '0001011': 9}
 
for tc in range(1, T +1):
    N, M = map(int, input().split())
    codes = []
    for _ in range(N):
        sec_code = input()
        if '1' in sec_code:
            for i in range(M-1, -1, -1):
                if sec_code[i] == '1':
                    codes.append(sec_code[i-55:i+1])
                    break
 
 
    result = 0
    ans = 0
    for i in range(8):
        c = codes[0][7*i: 7 * (i+1)]
        if c in secret_code:
            if (i+1) % 2 != 0:
                result += secret_code.get(c) * 3
                ans += secret_code.get(c)
            else:
                result += secret_code.get(c)
                ans += secret_code.get(c)
    if result % 10 == 0:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} 0')