def solution(n, s):
    # 모두 공평하게 값을 나눠준 상태에서 나머지를 각각 1씩 더해주는것이 최고의 집합
    if n > s:
        return [-1]
    
    p, q = divmod(s, n)
    answer = [p] * n
    
    for i in range(q):
        answer[i] += 1
        
    return sorted(answer)
