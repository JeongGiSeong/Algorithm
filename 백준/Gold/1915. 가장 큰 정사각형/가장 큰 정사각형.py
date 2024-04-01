import sys
input = sys.stdin.readline

# 1000x1000 크기에 전부 1이라고 가정
# 1x1=1000x1000개, 2x2=999x999개 ... 1000x1000=1x1개
# i^2 1...1000 = 약 3억개의 정사각형
# 즉, 완전탐색은 연산까지 고려하지 않아도 이미 시간초과

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]
dp = [[0] * M for _ in range(N)]

# DP(i, j) : (i, j) 칸을 우하단으로 하는 정사각형의 최대 크기
# DP(i, j) = min(DP(i-1, j), DP(i, j-1), DP(i-1, j-1)) + 1

for i in range(M):
    if arr[0][i] == '1':
        dp[0][i] = 1

for i in range(1, N):
    if arr[i][0] == '1':
        dp[i][0] = 1

    for j in range(1, M):
        if arr[i][j] == '1':
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, dp[i][j])

print(ans**2)