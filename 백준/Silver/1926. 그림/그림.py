from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)
visited = [[False] * M for _ in range(N)]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    area = 1
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=nx<M and 0<=ny<N:
                if board[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    area += 1
                    q.append((ny, nx))
    return area

cnt = 0
area = 0
for i in range(N):
    for j in range(M):
        if board[i][j] and not visited[i][j]:
            cnt += 1
            area = max(area, bfs(i, j))

print(cnt)
print(area)