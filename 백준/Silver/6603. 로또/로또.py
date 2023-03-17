import sys, time
read = sys.stdin.readline
# print(f"{end - start:.5f} sec")


stack = []
visited = []

def dfs(depth, start):
    if depth == 6:
        print(' '.join(map(str, stack)))
        return

    for i in range(start, len(s)):
        stack.append(s[i])
        dfs(depth+1, i + 1)
        stack.pop()

while True:
    s = list(map(int, read().split()))
    if s[0] == 0:
        break
    del s[0]

    # 이미 방문한 노드는 방문 불가능하므로 visited는 없어도 됨
    # visited = [False] * k
    dfs(0, 0)
    print() # 공백 한 줄