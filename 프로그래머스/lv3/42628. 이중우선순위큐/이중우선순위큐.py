import heapq

def solution(operations):
    queue = []
    
    for operation in operations:
        op, num = operation.split()
        if op == 'I':
            heapq.heappush(queue, int(num))
        if op == 'D':
            # 큐가 비어있으면 삭제 연산 실행 X
            if len(queue) == 0:
                continue

            if num == '1':
                # 최댓값 제거
                queue.remove(max(queue))
            else:
                # 최솟값 제거
                heapq.heappop(queue)
                    
    if len(queue) == 0:
        return [0, 0]
    else:
        return [max(queue), heapq.heappop(queue)]
                