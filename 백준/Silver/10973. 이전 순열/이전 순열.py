import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


# 이전 순열 찾기, 1초
# N(1~10000)이므로 DFS 사용 불가능(재귀 깊이)
# 이전 순열을 찾는 규칙을 구해야 함
# 2 3 1 4의 이전 순열은 2 1 4 3
# next permutation 알고리즘의 반대로 가볼까?
# 뒤에서부터 permut[i - 1] > permut[i]인 값을 타겟으로 설정 -> 3
# 타겟 기준으로 뒤에서부터 타겟보다 작은 값을 발견하면 swap
# 타겟 기준 뒷부분을 내림차순으로 정렬

n = int(read())
permut = list(map(int, read().split()))

for i in range(n - 1, 0, -1):
    if permut[i - 1] > permut[i]:
        target = i - 1
        break
else:
    print(-1)
    exit()

for i in range(n - 1, 0, -1):
    if permut[target] > permut[i]:
        permut[target], permut[i] = permut[i], permut[target]
        permut = permut[:target + 1] + sorted(permut[target+1:], reverse=True)
        break

print(*permut)