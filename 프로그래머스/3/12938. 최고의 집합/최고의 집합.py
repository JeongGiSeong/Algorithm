def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    quotient, remainder = divmod(s, n)
    
    for i in range(n-remainder):
        answer.append(quotient)
    for i in range(remainder):
        answer.append(quotient+1)
        
    return answer

print(solution(4, 99))
