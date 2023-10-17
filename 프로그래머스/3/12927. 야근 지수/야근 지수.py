import heapq

def solution(n, works):
    # 최대한 works를 비슷하게 만들기
    
    if n >= sum(works):
        return 0
    answer = 0
    # 기본 값인 최소 힙에서 최대 힙으로 변경
    works = [-w for w in works]
    heapq.heapify(works)
    while n > 0:
        max_val = heapq.heappop(works)
        heapq.heappush(works, max_val+1)
        n -= 1

    for w in works:
        answer += w ** 2
    return answer