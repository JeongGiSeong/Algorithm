import sys
input = sys.stdin.readline

# 누적합 문제
n = int(input())
pre = [[0]*(n+1) for _ in range(n+1)]

# (i, j)까지의 누적합 구하기
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, n+1):
        pre[i][j] = pre[i][j-1] + pre[i-1][j] - pre[i-1][j-1] + arr[j-1]

max_profit = float('-inf')
# K x K 크기의 정사각형을 순회하며 최대 이익 계산
for k in range(1, n+1):
    for i in range(k, n+1):
        for j in range(k, n+1):
            profit = pre[i][j] - pre[i-k][j] - pre[i][j-k] + pre[i-k][j-k]
            max_profit = max(max_profit, profit)
            
print(max_profit)
