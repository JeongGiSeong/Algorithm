# 최악의 경우 : 200,000,000 * 200,000,000
# 이진 탐색을 사용할 경우 O(nlogm)이 되며, n은 디딤돌의 개수, m은 디딤돌에 적힌 숫자의 최댓값
# O(n) 방법이 있다? 슬라이딩 인덱스

from collections import deque
def solution(stones, k):
    n = len(stones)
    deque_k = deque()
    deque_k.append(0)
    
    for i in range(1, k):
        # 뒤쪽에 필요 없는 애들 다 제거
        while deque_k and stones[deque_k[-1]] < stones[i]:
            deque_k.pop()
        
        # 비었거나, 값이 더 큰 경우에만 집어넣기
        if not deque_k or stones[deque_k[-1]] >= stones[i]:
            deque_k.append(i)
    
    answer = stones[deque_k[0]]
    
    for i in range(k, n):
        # 뒤쪽 제거
        while deque_k and stones[deque_k[-1]] < stones[i]:
            deque_k.pop()
        
        # 앞쪽 제거
        while deque_k and deque_k[0] <= i - k:
            deque_k.popleft()
        
        # 더 큰 경우에만 집어넣기
        if not deque_k or stones[deque_k[-1]] >= stones[i]:
            deque_k.append(i)
        
        answer = min(answer, stones[deque_k[0]])
    return answer   