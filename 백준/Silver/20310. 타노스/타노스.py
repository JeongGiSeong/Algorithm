import sys, collections
input = sys.stdin.readline

# 앞에서부터 뒤로 가면서 1을 제거(1개수의 절반만큼)
# 뒤에서부터 앞으로 오면서 0을 제거(0 개수의 절반만큼)

S = list(input().strip())
cnt = collections.Counter(S)

cnt0 = cnt['0'] // 2
cnt1 = cnt['1'] // 2

# 앞에서부터 1을 제거
for i in range(len(S)):
    if cnt1 == 0:
        break
    if S[i] == '1':
        del S[i]
        cnt1 -= 1

# 뒤에서부터 0을 제거
for i in range(len(S)-1, -1, -1):
    if cnt0 == 0:
        break
    if S[i] == '0':
        del S[i]
        cnt0 -= 1

print(''.join(S))
