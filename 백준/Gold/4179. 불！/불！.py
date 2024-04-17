from collections import deque

R, C = map(int, input().split())
maze = [input() for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dist_f = [[-1] * C for _ in range(R)]
dist_j = [[-1] * C for _ in range(R)]
q_f = deque()
q_j = deque()

for r in range(R):
    for c in range(C):
        if maze[r][c] == 'F':
            q_f.append((r, c))
            dist_f[r][c] = 0
        if maze[r][c] == 'J':
            q_j.append((r, c))
            dist_j[r][c] = 0

while q_f:
    y, x = q_f.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < R and 0 <= nx < C and maze[ny][nx] != '#' and dist_f[ny][nx] == -1:
            dist_f[ny][nx] = dist_f[y][x] + 1
            q_f.append((ny, nx))

while q_j:
    y, x = q_j.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not (0 <= ny < R) or not (0 <= nx < C):  # 탈출 확인
            print(dist_j[y][x] + 1)
            exit(0)

        if maze[ny][nx] == '.' and dist_j[ny][nx] == -1:
            if dist_f[ny][nx] == -1 or dist_f[ny][nx] > dist_j[y][x] + 1:  # 불에 타기 전에 이동할 수 있는지 확인
                dist_j[ny][nx] = dist_j[y][x] + 1
                q_j.append((ny, nx))

print('IMPOSSIBLE')
