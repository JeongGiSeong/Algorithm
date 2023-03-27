import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")



### DFS 풀이 ###
N = int(read())
# 정사각형 지도 5 ≤ N ≤ 25
graph = []
num = []

for i in range(N):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt

    if x>=N or x<0 or y>=N or y<0:
        return False

    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

cnt, ans = 0, 0
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            ans += 1
            num.append(cnt)
            cnt = 0 # cnt 초기화

num.sort()
print(ans)
print(*num, sep='\n')
