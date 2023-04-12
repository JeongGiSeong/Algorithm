import sys
from collections import deque
read = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        curr = queue.popleft()
        for i,cost in tree[curr]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[curr] + cost
N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    start,end,weight = map(int,input().split())
    tree[start].append([end,weight])
    tree[end].append([start,weight])
    

dist = [-1] * (N + 1)
dist[1] = 0
bfs(1)
start = dist.index(max(dist))
dist = [-1] * (N + 1)
dist[start] = 0
bfs(start)
print(max(dist))