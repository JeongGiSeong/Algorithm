import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


N = int(input())
arr = list(input())

S = [[0]*N for _ in range(N)]

for i in range(N) :
    for j in range(i, N) :
        temp = arr.pop(0)
        if temp == '+' :
            S[i][j] = 1
        elif temp == '-' :
            S[i][j] = -1

result = [0 for _ in range(N)]


def check(idx) :
    hap = 0
    for i in range(idx, -1, -1) :
        hap += result[i]
        if hap == 0 and S[i][idx] != 0 :
            return False
        elif hap < 0 and S[i][idx] >= 0 :
            return False
        elif hap > 0 and S[i][idx] <= 0 :
            return False
    return True

def dfs(idx) :
    if idx == N :
        return True

    # 범위가 -10 ~ 10이면 시간과 가능성 높음
    for i in range(11) :
        result[idx] = S[idx][idx] * i
        if check(idx) and dfs(idx+1) :
            return True
    return False

dfs(0)
print(*result)