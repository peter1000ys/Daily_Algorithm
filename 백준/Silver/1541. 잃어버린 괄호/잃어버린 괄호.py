first = input().split('-')

all_num = []

for num in first:
    sum_ = 0
    second = num.split('+')
    for num2 in second:
        sum_ += int(num2)
    all_num.append(sum_)

n = all_num[0]
for i in range(1,len(all_num)):
    n -= all_num[i]
print(n)