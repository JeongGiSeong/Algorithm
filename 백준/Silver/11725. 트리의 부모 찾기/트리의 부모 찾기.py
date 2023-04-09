import sys
from collections import deque
read = sys.stdin.readline


N = int(read()) # N은 노드의 개수
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1) # 처음 방문한 노드의 전 노드가 부모

for _ in range(N-1):
    a, b = map(int, read().split())
    tree[a].append(b)
    tree[b].append(a)

sys.setrecursionlimit(10**6)
def dfs(v):
    for i in tree[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

dfs(1)

print(*visited[2:], sep='\n')