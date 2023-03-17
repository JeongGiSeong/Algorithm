import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


n = int(read())
w = [list(map(int, read().split())) for _ in range(n)]

# (2 ≤ N ≤ 10)
# 각 행렬의 성분은 1,000,000 이하의 양의 정수이며, 갈 수 없는 경우는 0이 주어진다.

visited = [False] * n
ans = sys.maxsize

def dfs(depth, node, cost):
    global ans

    if depth == n-1 and w[node][0] != 0:
        ans = min(ans, cost + w[node][0])
        return

    for next_node in range(n):
        if not visited[next_node] and w[node][next_node] != 0:
            visited[next_node] = True
            dfs(depth+1, next_node, cost+w[node][next_node])
            visited[next_node] = False

visited[0] = True
dfs(0, 0, 0)
print(ans)