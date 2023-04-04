import sys
from collections import deque
read = sys.stdin.readline


#  N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)
N, K = map(int, read().split())
dist = [0] * 100001
move = [0] * 100001

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()

        if x == K:
            print(dist[x])
            return

        # x*2의 가중치가 0이기 때문에 가장 먼저 큐에 들어가야 함
        # appendleft를 사용하거나 x*2를 먼저 연산해줘야 함
        for nx in (x*2, x-1, x+1):
            if 0<=nx<=100000 and not dist[nx]:
                dist[nx] = (dist[x]+1) if nx != x*2 else (dist[x])
                q.append(nx)

bfs(N)