import heapq
import sys

input = sys.stdin.readline

# 최대 힙과 최소 힙 초기화
max_heap = [] # 중앙값보다 작거나 같은 값
min_heap = [] # 중앙값보다 큰 값

for _ in range(int(input())):
    num = int(input())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))
    
    # 최소 힙의 최소값이 최대 힙의 최대값보다 작은 경우 두 힙의 원소를 교체
    # -> 중간값이 항상 최대 힙의 root 값(가장 큰 값)
    if min_heap and max_heap[0][1] > min_heap[0][0]:
        max_val = heapq.heappop(max_heap)[1]
        min_val = heapq.heappop(min_heap)[0]
        heapq.heappush(max_heap, (-min_val, min_val))
        heapq.heappush(min_heap, (max_val, max_val))
    
    print(max_heap[0][1])