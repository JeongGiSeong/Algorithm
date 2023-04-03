import sys
from collections import deque
read = sys.stdin.readline


# 2초, 192MB
# BFS를 사용하면 될 듯 -> 최대 100x100. 
# BFS는 최대 O(n**2)이므로 1억번 연산 -> 1초
# 섬 번호 구분 bfs와 거리 계산 bfs 총 2개를 만들어야 함

N = int(read())
graph = [list(map(int, read().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 섬 번호 매기는 BFS
def marking(i, j, mark):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    graph[i][j] = mark
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = mark
                visited[nx][ny] = True
                q.append((nx, ny))

# 거리 계산하는 BFS
def getDist(i, j, now):
    q = deque()
    q.append((i, j, 0))
    while q:
        x, y, cnt = q.popleft()
        # 물이 아니면서 같은 타일이 아니면 -> 다른 섬이라는 의미
        if graph[x][y] != 0 and graph[x][y] != now:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] != now:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))
    return sys.maxsize

n = 1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            marking(i, j, n)
            n += 1

ans = sys.maxsize
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            visited = [[False] * N for _ in range(N)]
            ans = min(ans, getDist(i, j, graph[i][j]))

print(ans - 1)

