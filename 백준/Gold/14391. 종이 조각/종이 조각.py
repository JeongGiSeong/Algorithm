import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# n행, m열
n, m = map(int, read().split())
paper = [list(map(int, read().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 0, 0, 1, 2, 3]
dy = [0, 1, 2, 3, 0, 0, 0]

ans = 0

# (x, y)에서 (x, ny) 또는 (nx, y)까지 사용된 곳이 있는지를 체크하기 위한 함수
def isVisited(x, y, nx, ny):
    for i in range(x, nx + 1):
        if visited[i][y]: # 이미 사용된 곳이라면 True 반환
            return True

    for i in range(y, ny + 1):
        if visited[x][i]: # 이미 사용된 곳이라면 True 반환 
            return True

    return False

# visited 배열을 flag로 바꿔주기 위한 메서드 
def toggleVisited(x, y, nx, ny, flag):
    for i in range(x, nx + 1):
        visited[i][y] = flag

    for i in range(y, ny + 1):
        visited[x][i] = flag


# (x, y)에서 (x, ny) 또는 (nx, y)까지의 숫자를 구하기 위한 메서드 
def calcNum(x, y, nx, ny):
    calc = paper[x][y]

    for i in range(x + 1, nx + 1):
        calc = calc * 10 + paper[i][y]

    for i in range(y + 1, ny + 1):
        calc = calc * 10 + paper[x][i]

    return calc

def dfs(idx: int, total: int):
    global ans

    if idx == n * m:
        ans = max(ans, total)
        return

    # idx를 기준으로 (x, y) 좌표를 구한다
    x = idx // m
    y = idx % m 

    if visited[x][y]: # 이미 사용된 곳이면 다음 인덱스로 함수 호출
        dfs(idx + 1, total)
        return

    for i in range(7):
        nx = x + dx[i]
        ny = y + dy[i]

        # x, y부터 nx, ny까지 범위를 넘었거나 이미 방문했으면 continue
        if nx >= n or ny >= m or isVisited(x, y, nx, ny):
            continue

        # 백트래킹 
        toggleVisited(x, y, nx, ny, True)
        dfs(idx + 1, total + calcNum(x, y, nx, ny))
        toggleVisited(x, y, nx, ny, False)

dfs(0, 0)
print(ans)


### 비트마스크 풀이 804ms ###
# # n행, m열
# n, m = map(int, input().split())

# paper = []
# for _ in range(n):
#     paper.append(list(map(int, input())))

# ans = 0

# # ** 0이면 세로, 1이면 가로로 가정 **
# for i in range(1 << n*m):
#     total = 0
#     #가로합 계산
#     for row in range(n):
#         rowsum = 0
#         for col in range(m):
#             # idx는 2차원 행렬을 1줄로 만들었을때의 인덱스
#             idx = row*m + col
#             if i & (1 << idx) != 0: #(0아니면 가로로 더한다)
#                 rowsum = rowsum * 10 + paper[row][col]
#             else:
#                 total += rowsum
#                 rowsum = 0
#         total += rowsum

#     #세로합 계산
#     for col in range(m):
#         colsum = 0
#         for row in range(n):
#             idx = row*m + col
#             if i & (1 << idx) == 0: #(0이면 세로로 더한다)
#                 colsum = colsum * 10 + paper[row][col]
#             else:
#                 total += colsum
#                 colsum = 0
#         total += colsum

#     ans = max(ans, total)

# print(ans)
