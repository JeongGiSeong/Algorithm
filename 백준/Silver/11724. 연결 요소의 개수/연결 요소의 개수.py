import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# 정점의 개수 N과 간선의 개수 M
#  (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
#  (1 ≤ u, v ≤ N, u ≠ v)
n, m = map(int, read().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, read().split())
    graph[u][v] = graph[v][u] = True

sys.setrecursionlimit(10 ** 6)
def dfs(v):
    visited[v] = True
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i]:
            visited[i] = True
            dfs(i)

from collections import deque
def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        pop = queue.popleft()
        for i in range(1, n + 1):
            if not visited[i] and graph[pop][i]:
                visited[i] = True
                queue.append(i)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)
        # bfs(i)

print(cnt)