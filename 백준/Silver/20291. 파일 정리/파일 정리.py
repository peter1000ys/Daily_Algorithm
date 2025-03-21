import sys

input = sys.stdin.readline

n = int(input())

new_dict = {}

for _ in range(n):
    file = input().rstrip()
    type_name = ''
    file_type = False

    for a in file:

        if file_type:
            type_name += a
        if a == '.':
            file_type = True
    if type_name in new_dict:
        new_dict[type_name] += 1
    else:
        new_dict[type_name] = 1
new_dict = sorted(new_dict.items())


for item in new_dict:
    print(item[0]+' '+str(item[1]))


