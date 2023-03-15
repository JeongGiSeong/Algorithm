import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


n = int(read())
array = list(map(int, read().split()))
stack = []
visited = [False] * n
ans = 0

def dfs(depth: int):
    global ans
    if depth == n:
        s = 0
        for i in range(n - 1):
            s += abs(stack[i] - stack[i + 1])
        ans = max(ans, s)
        # print(' '.join(map(str, stack)))///
        return

    for i in range(n):
        # 지금 문제점 : visited를 사용하지 않아서 중복을 못 거름
        # if array[i] not in stack:
        
        if not visited[i]:
            visited[i] = True
            stack.append(array[i])
            dfs(depth + 1)
            visited[i] = False
            stack.pop()

dfs(0)
print(ans)
