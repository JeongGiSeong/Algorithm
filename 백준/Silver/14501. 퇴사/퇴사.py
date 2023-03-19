import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


# 누적 상담일 + T[i] <= N
# 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 
# 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

n = int(read())
schedule = [list(map(int, read().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    for j in range(i + schedule[i][0], n + 1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[n])