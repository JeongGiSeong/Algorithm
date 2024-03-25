import heapq as hq
import sys

input = sys.stdin.readline

min_heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        hq.heappush(min_heap, (abs(x), x))
    else:
        print(hq.heappop(min_heap)[1] if min_heap else 0)