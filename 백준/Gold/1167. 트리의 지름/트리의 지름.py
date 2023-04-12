import sys
from collections import deque
read = sys.stdin.readline


N = int(read())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    arr = list(map(int, read().split()))
    i = 1
    while arr[i] != -1:
        # 양방향 정보가 다 주어지기 때문에 단방향만 넣으면 됨
        tree[arr[0]].append([arr[i], arr[i+1]])
        i += 2

def bfs(start):
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for node, weight in tree[cur]:
            if dist[node] == -1:
                dist[node] = dist[cur] + weight
                q.append(node)

dist = [-1] * (N + 1)
dist[1] = 0
bfs(1)
start = dist.index(max(dist))
dist = [-1] * (N + 1)
dist[start] = 0
bfs(start)
print(max(dist))
