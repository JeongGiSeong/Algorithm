import sys
input = sys.stdin.readline

# 완전탐색: O(2^n)
# dp[i][j]: i번째 사각형을 j 방향으로 놨을 때 위쪽의 둘레 최대값

n = int(input())

dp = [[0, 0] for _ in range(n)]
rect = [list(map(int, input().split())) for _ in range(n)]

dp[0][0] = rect[0][0]
dp[0][1] = rect[0][1]
for i in range(1, n):
    dp[i][0] = rect[i][0] + max(dp[i-1][0] + abs(rect[i-1][1] - rect[i][1]), dp[i-1][1] + abs(rect[i-1][0] - rect[i][1]))
    dp[i][1] = rect[i][1] + max(dp[i-1][0] + abs(rect[i-1][1] - rect[i][0]), dp[i-1][1] + abs(rect[i-1][0] - rect[i][0]))
    
print(max(dp[n-1]))
