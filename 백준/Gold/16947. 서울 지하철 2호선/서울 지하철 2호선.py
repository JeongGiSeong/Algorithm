import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# 각 역과 순환선 사이의 거리를 구하라
# 순환선 구하는 건 DFS, 거리는 BFS 사용
N = int(read()) # N(3 ≤ N ≤ 3,000)
graph = [[] for _ in range(N + 1)]
cycle = [False] * (N + 1)
visited = [False] * (N + 1)
pre = [False] * (N + 1)
hasCycle = False

for _ in range(N):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

sys.setrecursionlimit(10 ** 6)
def dfs(prev, cur):
    global hasCycle

    visited[cur] = True
    
    for v in graph[cur]:
        if hasCycle: return
        if visited[v]:
            if v != pre[cur]:
                cycle[cur] = True
                hasCycle = True
                while cur != v:
                    # 기록 역추적하면서 사이클 저장
                    cycle[pre[cur]] = True
                    cur = pre[cur]
                return
        else:
            # pre에 지나왔던 노드 기록
            pre[v] = cur
            dfs(cur, v)

dfs(1, 1)

from collections import deque
dist = [-1] * (N + 1)
q = deque()
for i in range(1, N + 1):
    if cycle[i]:
        q.append(i)
        dist[i] = 0
while q:
    v = q.popleft()
    for i in graph[v]:
        if dist[i] == -1:
            q.append(i)
            dist[i] = dist[v] + 1

print(*dist[1:])