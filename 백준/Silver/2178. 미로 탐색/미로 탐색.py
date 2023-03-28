import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


### DFS 풀이 ###
sys.setrecursionlimit(10**6)
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

ans = 0
def dfs(x, y, cnt):
    global ans

    if x<0 or x>=n or y<0 or y>=m:
        return

    if x==(n-1) and y==(m-1):
        ans = cnt
        return
    
    if maze[x][y] == 1:
        maze[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny, cnt + 1)

### BFS 풀이 ###
from collections import deque
def bfs():
    queue = deque()
    # (0, 0)이 시작점
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and maze[nx][ny]==1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

        
# N개의 줄에는 M개의 정수로 미로가 주어진다.
n, m = map(int, read().split())
maze = [list(map(int, input())) for _ in range(n)]

# dfs(0, 0, 0)
# # 마지막 칸 +1
# print(ans + 1)

bfs()
print(maze[n-1][m-1])