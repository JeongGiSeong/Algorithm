import heapq
    
def solution(n, works):
    # 최대한 works를 비슷하게 만들기
    
    if sum(works) <= n:
        return 0
    
    answer = 0
    # 기본값인 최소 힙에서 최대 힙으로 변환
    works = [-w for w in works]
    heapq.heapify(works)
    while n > 0:
        max_val = heapq.heappop(works)
        heapq.heappush(works, max_val+1)
        n -= 1

    return sum(list(map(lambda x: x**2, works)))    
    
    
    
    ########################### 효율성 테스트 실패 (시간 초과) ##########################################
    if n > sum(works):
        return 0
    while n:
        m = max(works)
        if m > 0:
            works[works.index(m)] -= 1
            n -= 1
        
    return sum(list(map(lambda x: x**2, works)))