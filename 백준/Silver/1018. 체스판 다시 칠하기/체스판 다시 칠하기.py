# N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 어떤 알고리즘을 사용해야 할까?
# 완전탐색? 50x50 크기라 될듯?
# DP? 이건 아닌 듯. 완전탐색 방향으로 가보자.

# board[n][m]을 시작으로 다시 칠해야 하는 정사각형의 최소 개수 반환
def cal(n, m, color):
    cnt = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            # board[n][m]을 흰색이라고 가정하면
            # n이 짝수일 때, m이 홀수면 흰색, 짝수면 검은색임
            # n이 홀수일 때, m이 홀수면 검은색, 짝수면 흰색임
            if i % 2 == 0:
                if j % 2 == 0:
                    if board[i][j] != color:
                        cnt += 1
                else:
                    if board[i][j] == color:
                        cnt += 1
            else:
                if j % 2 == 0:
                    if board[i][j] == color:
                        cnt += 1
                else:
                    if board[i][j] != color:
                        cnt += 1
    return cnt


ans = float('inf')
for i in range(N-7):
    for j in range(M-7):
        ans = min(ans, cal(i, j, 'W'), cal(i, j, 'B'))

print(ans)