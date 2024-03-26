from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

def is_vaild_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def bfs():
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    dq = deque()
    dq.append((0, 0, 1))
    while dq:
        y, x, d = dq.popleft()

        if y == N - 1 and x == M - 1:
            return d

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_vaild_coord(ny, nx) and board[ny][nx] == '1' and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.append((ny, nx, d + 1))

    return -1

print(bfs())