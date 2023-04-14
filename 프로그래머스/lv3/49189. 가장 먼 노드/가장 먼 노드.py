from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    # 노드 2~20000, 양방향 간선, 50000개 이하 간선 개수
    # BFS : O(V + E)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    dist = [-1] * (n + 1)
    dist[1] = 0
    
    # BFS
    q = deque()
    q.append(1)
    while q:
        curr = q.popleft()
        for v in graph[curr]:
            if dist[v] == -1:
                dist[v] = dist[curr] + 1
                q.append(v)

    answer = dist.count(max(dist))
    return answer

    
    