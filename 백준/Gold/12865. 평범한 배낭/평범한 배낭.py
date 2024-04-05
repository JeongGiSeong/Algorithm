import sys
input = sys.stdin.readline

# 냅색 알고리즘
# 참고 : https://howudong.tistory.com/106

N, W = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(N)] #(weight, value)
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
wv.insert(0, (0, 0))

# dp[i][w]: 최대무게가 w인 배낭에 첫 번째부터 i번째 물건까지 고려했을 때의 최대 가치
# 항목 i를 배낭에 넣지 않는 경우: dp[i][w] = dp[i-1][w]
# 항목 i를 배낭에 넣는 경우: dp[i][w] = dp[i-1][w-weights[i]] + values[i] (단, w-weights[i]가 0 이상인 경우)

for i in range(1, N+1):
    for w in range(1, W+1):
        weight = wv[i][0]
        value = wv[i][1]
        if weight <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
        else:
            dp[i][w] = dp[i-1][w]

print(dp[N][W])