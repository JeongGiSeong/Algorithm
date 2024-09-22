import sys, collections
input = sys.stdin.readline

N = int(input())
A, P_A, B, P_B = map(int, input().split())

# 완전탐색? 최악의 경우 O(N^2) -> O(10^14) 시간초과
# DP도 완전탐색과 마찬가지의 이유로 시간 초과

dp = [(0, 0, 0)] * (N + 1)

for i in range(N + 1):
    if i >= P_A:
        if dp[i - P_A][0] + A > dp[i][0]:
            dp[i] = (dp[i - P_A][0] + A, dp[i - P_A][1] + 1, dp[i - P_A][2])

    if i >= P_B:
        if dp[i - P_B][0] + B > dp[i][0]:
            dp[i] = (dp[i - P_B][0] + B, dp[i - P_B][1], dp[i - P_B][2] + 1)

max_power, x, y = dp[N]
print(x, y)

####### 오답노트 ########
# DP[i]: i원을 사용하여 얻을 수 있는 최대 전투력 및 탱, 딜의 수
# DP도 시도 해 봤는데 완전탐색과 마찬가지의 이유로 시간 초과