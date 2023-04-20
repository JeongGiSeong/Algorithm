def solution(array, commands):
    answer = []
    
    for cmd in commands:
        s, e, loc = cmd
        answer.append(sorted(array[s-1:e])[loc-1])
    return answer