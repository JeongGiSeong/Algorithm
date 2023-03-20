import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


n = int(read())
member = [list(map(int, read().split())) for _ in range(n)]

# dfs? -> N이 20까지라 안 될 듯
# 근데 백트래킹 문제라네? -> depth가 n//2라 10까지라고 보는게 맞아서 가능

visited = [False] * n
ans = sys.maxsize
def dfs(depth: int, idx: int):
    global ans
    
    if depth == n // 2:
        # print(' '.join(map(str, )))
        p1, p2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    p1 += member[i][j]
                elif not visited[i] and not visited[j]:
                    p2 += member[i][j]
        ans = min(ans, abs(p1 - p2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(ans)