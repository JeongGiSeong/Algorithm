import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# 2초, 256mb
# 부분수열의 합
# (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 
# 주어지는 정수의 절댓값은 100,000을 넘지 않는다.
# ** 1 2 3 5가 주어졌을 때 2 5 처럼 건너뛰어도 순서만 맞으면 부분수열 **

##### dfs 풀이 #####
# n, s = map(int, read().split())
# sequence = list(map(int, read().split()))

# cnt = 0
# stack = []
# visited = [False] * n
# def dfs(depth: int, idx: int):
#     global cnt

#     if depth > 0:
#         if sum(stack) == s:
#             # print(*stack)
#             cnt += 1

#     if depth == n:
#         return

#     for i in range(idx, n):
#         if not visited[i]:
#             visited[i] = True
#             stack.append(sequence[i])
#             dfs(depth + 1, i + 1)
#             visited[i] = False
#             stack.pop()

# dfs(0, 0)
# print(cnt)

##### 비트마스크 풀이 #####
n, s = map(int, read().split())
sequence = list(map(int, read().split()))

ans = 0
# 모든 경우의 수 (n이 5면 2**5 -> 32)
for i in range(1, (1 << n)):
    total = 0
    for j in range(n):
        # check
        if (i & (1 << j)) > 0:
            total += sequence[j]
    if total == s:
        ans += 1

print(ans)