import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(lambda x: x-1, map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

# 최단 거리 문제니까 BFS, 플로이드와샬
kevin = []
ans = (-1, float('inf'))

def bfs(start, goal):
    chk = [False] * N
    chk[start] = True
    dq = deque()
    dq.append((start, 0))
    while dq:
        now, d = dq.popleft()
        if now == goal:
            return d
        for nxt in graph[now]:
            if not chk[nxt]:
                chk[nxt] = True
                dq.append((nxt, d+1))

def get_kevin(start):
    total = 0
    for i in range(N):
        if i != start:
            total += bfs(start, i)
    return total

for i in range(N):
    kevin.append(get_kevin(i))

for i, v in enumerate(kevin):
    if ans[1] > v:
        ans = (i, v)

print(ans[0] + 1)