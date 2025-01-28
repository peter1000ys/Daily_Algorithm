def solution(array, commands):
    
    answer = []
    for command in commands:
        i, j, k = command
        sorted_list = sorted(array[i-1:j])
        answer.append(sorted_list[k-1])
    
    return answer