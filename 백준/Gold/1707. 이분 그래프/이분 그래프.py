import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")



#### BFS 풀이 ####
from collections import deque
def bfs():
    # 테스트케이스 개수
    k = int(read())

    for _ in range(k):
        # 정점의 개수 v, 간선의 개수 e
        v, e = map(int, read().split())
        graph = [[] for _ in range(v + 1)]
        visited = [0] * (v + 1)

        for _ in range(e):
            a, b = map(int, read().split())
            graph[a].append(b)
            graph[b].append(a)

        queue = deque()
        GROUP= 1
        flag = False
        for i in range(1, v + 1):
            if visited[i] == 0:
                queue.append(i)
                visited[i] = GROUP
                while queue:
                    pop = queue.popleft()
                    for j in graph[pop]:
                        if visited[j] == 0: # 방문하지 않은 정점이면 큐에 삽입
                            queue.append(j)
                            visited[j] = -1 * visited[pop] # 현재 노드와 다른 그룹 지정
                        elif visited[j] == visited[pop]: # 이미 방문한 경우에 동일 그룹에 속하면 'NO'
                            flag = True

        print('YES' if not flag else 'NO')


#### DFS 풀이 ####
sys.setrecursionlimit(10 ** 6)
# 테스트케이스 개수
k = int(read())
def dfs(v, group):
    global error

    if error:
        return

    visited[v] = group  # 해당 그룹으로 등록
    for i in graph[v]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[v] == visited[i]:  # 인접한데 같은 그룹이라면
            error = True  # 에러값 True
            return  # 그후 재귀 리턴


for _ in range(k):
    # 정점의 개수 v, 간선의 개수 e
    v, e = map(int, read().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    error = False

    for _ in range(e):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if not visited[i] and not error:  # 만약 아직 방문하지 않았다면
            dfs(i, 1)  # dfs를 돈다.
    print('YES' if not error else 'NO')