def solution(array, commands):
    answer = []
    
    for cmd in commands:
        s = cmd[0] - 1
        e = cmd[1]
        loc = cmd[2] - 1
        answer.append(sorted(array[s:e])[loc])
    return answer