import sys
input = sys.stdin.readline

N = int(input())
costs = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    costs[i] = list(map(int, input().split()))

# dp[i][j]: i번째 집이 j색일 때 모든 집을 칠하는 비용의 최솟값
# dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + costs[i][R]
# dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + costs[i][G]
# dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + costs[i][B]
R, G, B = 0, 1, 2
dp = [[0] * 3 for _ in range(1001)]

dp[1] = costs[1]
for i in range(2, N+1):
    dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + costs[i][R]
    dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + costs[i][G]
    dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + costs[i][B]


print(min(dp[N][R], dp[N][G], dp[N][B]))