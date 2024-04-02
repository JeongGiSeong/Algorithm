N = int(input())

dp = [0] * (N+1)
pre = [0] * (N+1)

dp[1] = 0
for i in range(2, N+1):
    dp[i] = dp[i-1]+1
    pre[i] = i-1
    if i % 2 == 0 and dp[i] > dp[i//2]+1:
        dp[i] = dp[i//2]+1
        pre[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i//3]+1:
        dp[i] = dp[i//3]+1
        pre[i] = i // 3

print(dp[N])

# pre 배열을 사용하여 경로를 역추적
path = []
cur = N
while cur != 0:
    path.append(cur)
    cur = pre[cur]
print(" ".join(map(str, path)))