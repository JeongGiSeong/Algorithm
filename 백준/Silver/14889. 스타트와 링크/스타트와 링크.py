import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# ** 기존 백트래킹 풀이 **
# n = int(read())
# member = [list(map(int, read().split())) for _ in range(n)]

# # dfs? -> N이 20까지라 안 될 듯
# # 근데 백트래킹 문제라네? -> depth가 n//2라 10까지라고 보는게 맞아서 가능

# visited = [False] * n
# ans = sys.maxsize
# def dfs(depth: int, idx: int):
#     global ans
    
#     if depth == n // 2:
#         # print(' '.join(map(str, )))
#         p1, p2 = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i] and visited[j]:
#                     p1 += member[i][j]
#                 elif not visited[i] and not visited[j]:
#                     p2 += member[i][j]
#         ans = min(ans, abs(p1 - p2))
#         return

#     for i in range(idx, n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(depth + 1, i + 1)
#             visited[i] = False

# dfs(0, 0)
# print(ans)

# ** 비트마스크 풀이 **
# 시간초과가 발생하는 이유 : 1 3 5, 2 4 6 팀과 2 4 6, 1 3 5 팀은 같다.
# 중복을 해결해야 함.
n = int(read())
ability = [list(map(int, read().split())) for _ in range(n)]
ans = sys.maxsize

# 모든 경우의 수 : 2 ** 4 = 32
for i in range(1 << n):
    # 가정 1. 모든 경우의 수를 리스트에 넣었다뺐다하면서 시간초과
    cnt = 0
    for j in range(n):
        if i & (1 << j) > 0:
            cnt += 1

    if cnt != n // 2:
        continue

    start, link = [], []
    for j in range(n):
        if i & (1 << j) > 0:
            start.append(j)
        else:
            link.append(j)

    
    # 각 팀이 n//2로 구성되었을 때만
    st, li = 0, 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            st += ability[start[i]][start[j]] + ability[start[j]][start[i]]
            li += ability[link[i]][link[j]] + ability[link[j]][link[i]]
    ans = min(ans, abs(st - li))

print(ans)