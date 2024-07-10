import sys
input = sys.stdin.readline

# 완전탐색: O(2^n)
# dp[i][j]: i번째 사각형을 j 방향으로 놨을 때 위쪽의 둘레 최대값

n = int(sys.stdin.readline())
dp = [[0, 0] for _ in range(n+1)]
arr = [[0, 0] for _ in range(n+1)]

arr[1] = list(map(int, sys.stdin.readline().split()))
dp[1][0] = arr[1][0]
dp[1][1] = arr[1][1]

for i in range(2, n+1):
    arr[i] = list(map(int, sys.stdin.readline().split()))
    dp[i][0] = arr[i][0] + max(dp[i-1][0] + abs(arr[i-1][1] - arr[i][1]), dp[i-1][1] + abs(arr[i-1][0] - arr[i][1]))
    dp[i][1] = arr[i][1] + max(dp[i-1][0] + abs(arr[i-1][1] - arr[i][0]), dp[i-1][1] + abs(arr[i-1][0] - arr[i][0]))

print(max(dp[n]))