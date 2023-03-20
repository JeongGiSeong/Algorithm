import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


# 숫자 중복 X, 순서 고려
# 부등호 순서를 만족하는 정수 중 최댓값과 최솟값을 출력

n = int(read())
sign = list(map(str, read().split()))

ans = []
stack = []
visited = [False] * 10

def dfs(depth):
    # 가지치기
    for i in range(depth - 1):
        if sign[i] == '>':
            if not stack[i] > stack[i + 1]:
                return
        elif sign[i] == '<':
            if not stack[i] < stack[i + 1]:
                return

    if depth == n + 1:
        ans.append(''.join(map(str, stack)))
        # print(*stack)
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            dfs(depth + 1)
            visited[i] = False
            stack.pop()

dfs(0)
ans.sort()
print(ans[len(ans) - 1])
print(ans[0])
