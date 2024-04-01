import sys
input = sys.stdin.readline

# dp[i][j]: j개의 계단을 연속해서 밟고 i번째 계단까지 올랐을 때 점수의 최댓값
# dp[k][1] = max(dp[k-2][1], dp[k-2][2]) + S(k)
# -> 연속이 1이라는 것은 k-2 계단을 밟았다는 것
# dp[k][2] = dp[k-1][1] + S(k)
# -> 연속이 2라는 건 k-1 계단을 밟았다는 것.
#    dp[k-1][2]을 밟았다면 연속 3계단을 오른 거라 규칙에 위배

def solution(n):
    if n == 1:
        print(S[1])
        return
    dp[1][1] = S[1]
    dp[1][2] = 0
    dp[2][1] = S[2]
    dp[2][2] = S[1] + S[2]

    for i in range(3, N+1):
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + S[i]
        dp[i][2] = dp[i-1][1] + S[i]
    print(max(dp[n][1], dp[n][2]))
    return

# 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수
S = [0] * 301
dp = [[0] * 3 for _ in range(301)]

N = int(input())
for i in range(1, N+1):
    S[i] = int(input())

solution(N)