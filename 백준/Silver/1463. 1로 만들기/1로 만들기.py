N = int(input())

dp = [0] * (N+1)
# dp[i]: i를 1로 만드는데 필요한 연산 사용 횟수의 최솟값
# dp[i] = min(dp[i-1]+1, dp[i//3]+1, dp[i//2]+1)

dp[1] = 0
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])