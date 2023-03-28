import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
# 단, 2 ≤ M,N ≤ 1,000
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
from collections import deque
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

# 익은 토마토를 전부 큐에 넣어놓고 BFS를 하면
# 익은 토마토 근처로 1칸씩 익게 되니까 1 2 3 1 같은 상황을 고려하지 않아도 된다
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            queue.append([i, j])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
            matrix[nx][ny] = matrix[x][y] + 1
            queue.append([nx, ny])

for i in matrix:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)