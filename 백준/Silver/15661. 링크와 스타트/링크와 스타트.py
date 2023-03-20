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

    if depth > n // 2:
        return
    
    if depth > 0:
        # print(' '.join(map(str, )))
        p1, p2 = 0, 0
        for i in range(n- 1):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    p1 += member[i][j] + member[j][i]
                elif not visited[i] and not visited[j]:
                    p2 += member[i][j] + member[j][i]
        ans = min(ans, abs(p1 - p2))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

# 시간초과가 계속 발생하는 이유?
# 스타트 팀이 135고 링크팀이 246일때와 팀 순서가 바뀌었을때 
# 능력치차이가 같은데 이걸 계속 계산하고 있음
dfs(0, 0)
print(ans)