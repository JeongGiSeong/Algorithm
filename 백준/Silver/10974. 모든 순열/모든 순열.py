import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


# 1부터 N까지의 수로 이루어진 모든 순열 사전순 출력
# N(1~8) -> dfs 사용 가능

n = int(read())
permut = [i for i in range(1, n + 1)]
stack = []
visited = [False] * n

def dfs(depth: int):
    if depth == n:
        print(' '.join(map(str, stack)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(permut[i])
            dfs(depth + 1)
            stack.pop()
            visited[i] = False

dfs(0)