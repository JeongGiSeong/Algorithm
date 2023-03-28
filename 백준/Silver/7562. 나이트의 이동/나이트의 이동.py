import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


from collections import deque
def bfs(graph: list, l: int, start: list, end: list):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if [x, y] == end:
            print(graph[x][y])
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1


# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
T = int(read())

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
for _ in range(T):
    # 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300) | 체스판의 크기는 l × l
    # 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
    # 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
    L = int(read())
    start = list(map(int, read().split()))
    end = list(map(int, read().split()))
    graph = [[0] * L for _ in range(L)]

    bfs(graph, L, start, end)
