import sys, heapq
input = sys.stdin.readline

# 붙여서 만들 수 있는 수 중에 3번째로 작은 수
# 시간복잡도: O(n) 이하

n = int(input()) # 3 ≤ n ≤ 10^8
hq = []
for _ in range(n):
    heapq.heappush(hq, int(input()))
    
data = [heapq.heappop(hq) for _ in range(min(4, n))]

ans = []
for i in data:
    for j in data:
        if i != j:
            r = int(str(i) + str(j))
            ans.append(r)
ans.sort()

print(ans[2])