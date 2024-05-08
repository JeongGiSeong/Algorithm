from collections import deque
import sys
input = sys.stdin.readline

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
def bfs(n, m):
    q = deque([(n, m)])
    while q:
        y, x = q.popleft()

        for dy, dx in d:
            ny, nx = y + dy, x + dx

            if 0<=ny<N and 0<=nx<M:
                if ground[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        ground[Y][X] = 1

    cnt = 0
    for n in range(N):
        for m in range(M):
            if ground[n][m] and not visited[n][m]:
                cnt += 1
                visited[n][m] = True
                bfs(n, m)

    print(cnt)