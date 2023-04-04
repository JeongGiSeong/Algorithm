import sys
from collections import deque
read = sys.stdin.readline


#  N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)
N, K = map(int, read().split())
dist = [0] * 100001

# DFS로 풀어볼까? -> 가지치기를 엄청 잘하지 않으면 최악의 경우 시간 초과
# BFS로 풀자
def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()

        if x == K:
            print(dist[x])
            return
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=100000 and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs(N)