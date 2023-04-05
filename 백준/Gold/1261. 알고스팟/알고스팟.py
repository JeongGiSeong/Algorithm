import sys
from collections import deque
read = sys.stdin.readline


#1초 128MB
# 미로는 가로 M, 세로 N. 상하좌우 이동 가능. 벽 부수기 가능
# 0이 빈 방, 1이 벽.

M, N = map(int, read().split())
maze = [list(map(int, input())) for _ in range(N)]
weight = [[-1] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 가중치는 벽을 부순 횟수와 같다.
# 0->0 가중치:0
# 0->1 가중치:1
# 1->1 가중치:1
# 0-1 BFS 문제
# 즉, 덱을 이용하여 가중치가 0일 때는 appendleft
# 가중치가 1일 때는 append 하면
# 벽을 최소로 부수는 개수를 찾을 수 있다.
def bfs():
    q = deque()
    q.append([0, 0])
    weight[0][0] = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if weight[nx][ny] == -1:
                    if maze[nx][ny] == 0:
                        weight[nx][ny] = weight[x][y]
                        q.appendleft([nx, ny])
                    else:
                        weight[nx][ny] = weight[x][y] + 1
                        q.append([nx, ny])

bfs()
print(weight[N-1][M-1])