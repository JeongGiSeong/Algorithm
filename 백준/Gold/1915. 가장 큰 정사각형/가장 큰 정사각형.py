import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [list(map(int, input().strip())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

ans = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if adj[i-1][j-1] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans**2)
