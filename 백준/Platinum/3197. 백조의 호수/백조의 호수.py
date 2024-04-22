from collections import deque
import sys
input = sys.stdin.readline

def melt_bfs():
    while melt_q:
        y, x = melt_q.popleft()
        if board[y][x] == 'X':
            board[y][x] = '.'
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0<=nx<C and 0<=ny<R and not melt_visited[ny][nx]:
                melt_visited[ny][nx] = True
                if board[ny][nx] == 'X':
                    melt_nextq.append((ny, nx))
                else:
                    melt_q.append((ny, nx))

def swan_bfs():
    while swan_q:
        y, x = swan_q.popleft()
        if (y, x) == swan[1]:
            return True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0<=nx<C and 0<=ny<R and not swan_visited[ny][nx]:
                swan_visited[ny][nx] = True
                if board[ny][nx] == '.':
                    swan_q.append((ny, nx))
                else:
                    swan_nextq.append((ny, nx))
    return False

# 호수는 행이 R개, 열이 C개인 직사각형 모양
# '.'은 물 공간, 'X'는 빙판 공간, 'L'은 백조가 있는 공간

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
swan_visited = [[False] * C for _ in range(R)]
melt_visited = [[False] * C for _ in range(R)]
melt_q, swan_q, melt_nextq, swan_nextq = deque(), deque(), deque(), deque()
dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

swan = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'L':
            swan.append((r, c))
            board[r][c] = '.'
        if board[r][c] == '.':
            melt_visited[r][c] = True
            melt_q.append((r, c))
swan_q.append(swan[0])
swan_visited[swan[0][0]][swan[0][1]] = True

day = 0
while True:
    melt_bfs()
    if swan_bfs():
        print(day)
        break
    swan_q, melt_q = swan_nextq, melt_nextq
    swan_nextq, melt_nextq = deque(), deque()
    day += 1