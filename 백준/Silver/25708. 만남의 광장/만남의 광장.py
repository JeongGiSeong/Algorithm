import sys
input = sys.stdin.readline

# 2 ≤ N ≤ 100, 2 ≤ M ≤ 100
# 시간제한 1초, O(N^2)까지 가능
# 브루트포스: 4중 for문 / O(N^2 * M^2) / 1초 아슬아슬하게 되나?
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 아름다움: 4개의 길 합 + 4개 길에 둘러싸인 녹지의 칸
row_sum = [sum(row) for row in board]
col_sum = [sum(board[i][j] for i in range(N)) for j in range(M)]

max_beauty = float('-inf')

for up in range(N):
    for down in range(up + 1, N):
        for left in range(M):
            for right in range(left + 1, M):
                beauty = row_sum[up] + row_sum[down] + col_sum[left] + col_sum[right] # 길 칸
                beauty -= (board[up][left] + board[up][right] + board[down][left] + board[down][right]) # 겹치는 부분 제거
                beauty += (down - up - 1) * (right - left - 1) # 녹지 칸
                max_beauty = max(max_beauty, beauty)

print(max_beauty)