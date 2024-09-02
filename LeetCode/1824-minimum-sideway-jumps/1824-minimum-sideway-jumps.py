class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # 1 <= n <= 5 * 10^5 -> O(n^2)은 거의 3초라서 안됨
        # dp[i][j]: i번째 j라인까지 오면서 뛴 사이드 점프 횟수의 최솟값
        n = len(obstacles) - 1
        dp = [[float('inf')] * 3 for _ in range(n+1)]
        dp[0] = [1, 0, 1] # 2차선에서 시작

        for i in range(1, n + 1):
            for j in range(3):
                # 현재 라인에 장애물이 없으면 그대로
                if obstacles[i] != j + 1:
                    dp[i][j] = dp[i-1][j]

            for j in range(3):
                # 다른 라인에서 사이드 점프를 통해 오는 경우를 고려하여 최소값 계산
                if obstacles[i] != j + 1:
                    dp[i][j] = min(dp[i][j], dp[i][(j + 1) % 3] + 1, dp[i][(j + 2) % 3] + 1)

        return min(dp[n][0], dp[n][1], dp[n][2])