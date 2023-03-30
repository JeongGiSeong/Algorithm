import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# 둘째 줄부터 N개의 줄에 게임판의 상태가 주어진다.
N, M = map(int, read().split())
graph = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# DFS가 빠르려나 BFS가 빠르려나
##### DFS 풀이 #####
sys.setrecursionlimit(10**6)
def dfs(prev_x, prev_y, x, y):
    # 이미 방문한 곳을 또 방문했다는 건 사이클이 존재한다는 의미
    if visited[x][y]:
        print("Yes")
        exit()

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0<=nx<N and 0<=ny<M) or graph[nx][ny] != graph[x][y]:
            continue

        # 이전 위치와 같은 위치를 제외하고 탐색해야 함
        if (nx, ny) == (prev_x, prev_y):
            continue

        dfs(x, y, nx, ny)

for i in range(N):
    for j in range(M):
        # 사이클만 찾으면 되는 거라 모든 정점을 탐색할 필요 없음
        if not visited[i][j]:
            dfs(-1, -1, i, j)
print("No")