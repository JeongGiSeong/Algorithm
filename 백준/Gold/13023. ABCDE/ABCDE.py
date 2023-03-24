import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


n, m = map(int, input().split())
relations = [[] for i in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 표현
for _ in range(m):
    a, b = map(int, read().split())
    relations[a].append(b)
    relations[b].append(a)


def dfs(depth, idx):
    if depth == 4:
        print(1)
        exit()
    for i in relations[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i)
            visited[i] = False

# 노드를 순서대로 방문하며 dfs를 수행
for i in range(n):
    visited[i] = True
    dfs(0, i)
    visited[i] = False

print(0)