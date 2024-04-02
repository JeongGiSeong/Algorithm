#     0 1
# -------
# 0 | 1 0
# 1 | 0 1
# 2 | 1 1
# 3 | 1 2
# 4 | 2 3
# 5 | 3 5
# 6 | 5 8
# 피보나치를 DP로 푸는 것과 동일한 방식
# fibo[i] = fibo[i-1] + fibo[i-2]
import sys
input = sys.stdin.readline

cnt = [(0, 0)] * 41

cnt[0], cnt[1] = (1, 0), (0, 1)
for i in range(2, 41):
    cnt[i] = (cnt[i-1][0] + cnt[i-2][0], cnt[i-1][1] + cnt[i-2][1])

for _ in range(int(input())):
    print(*cnt[int(input())])