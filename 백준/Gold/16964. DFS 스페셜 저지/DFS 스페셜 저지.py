import sys
from collections import deque
read = sys.stdin.readline


N = int(read())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
answer = list(map(int, read().split()))

# 그래프 순서 변경
order = [0] * (N + 1)
for i in range(N):
    order[answer[i]] = i
# print(graph)
for i in range(N + 1):
    graph[i].sort(key=lambda x: order[x])
# print(graph)

stack = []
visited = [False] * (N + 1)
res = []
def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    res.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
        
dfs(1)
print(1 if answer == res else 0)
# print(res)