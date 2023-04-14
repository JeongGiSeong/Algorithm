def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    s = e = 0
    for start, end in targets:
        if start >= e:
            answer += 1
            e = end

    return answer 