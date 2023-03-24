import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")

from collections import deque

n, m, v = map(int, read().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)

def bfs(v):
    visited_bfs[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in range(1, n + 1):
            if not visited_bfs[i] and graph[pop][i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)