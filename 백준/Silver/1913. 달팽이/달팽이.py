N = int(input())
target = int(input())

matrix = [[0] * N for _ in range(N)]

x, y = N // 2, N // 2
matrix[x][y] = 1

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 2
direction = 0

# 이동 거리
step = 1

while num <= N * N:
    for _ in range(2):
        for _ in range(step):
            x += dx[direction]
            y += dy[direction]
            if 0 <= x < N and 0 <= y < N:
                matrix[x][y] = num
                num += 1
        direction = (direction + 1) % 4
    step += 1

for row in matrix:
    print(' '.join(map(str, row)))

for i in range(N):
    for j in range(N):
        if matrix[i][j] == target:
            print(i + 1, j + 1)
            break
