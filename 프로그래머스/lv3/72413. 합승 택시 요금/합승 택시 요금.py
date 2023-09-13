import sys, heapq

# 플로이드 와샬
def solution1(n, s, a, b, fares):
    graph = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for c, d, f in fares: # c와 d 사이 요금이 f
        graph[c][d] = f
        graph[d][c] = f
    
    # 합승 비용 계산
    for middle in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if start == end:
                    graph[start][end] = 0
                graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])
    
    ans = sys.maxsize
    for t in range(1, n+1):
        cost = graph[s][t] + graph[t][a] + graph[t][b]
        ans = min(ans, cost)
    
    return ans


# 다익스트라
def solution(n, s, a, b, fares):
    # 그래프를 초기화합니다. 각 지점 간의 요금을 딕셔너리 형태로 저장합니다.
    graph = {}
    for i in range(1, n + 1):
        graph[i] = {}
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
    
    def dijkstra(start):
        distances = {node: float('INF') for node in graph}
        distances[start] = 0
        queue = []
        # heapq로 우선순위 큐 구현
        heapq.heappush(queue, (0, start))
        while queue:
            # 큐에서 가장 작은 거리와 해당 정점을 꺼냅니다.
            current_distance, current_node = heapq.heappop(queue)
            # 현재 정점까지의 거리가 이미 저장된 거리보다 크다면 무시합니다.
            if distances[current_node] < current_distance:
                continue
            # 현재 정점과 인접한 정점들에 대해 반복합니다.
            for adjacent, weight in graph[current_node].items():
                # 현재 정점까지의 거리와 인접한 정점까지의 요금을 더합니다.
                distance = current_distance + weight
                # 이 값이 기존에 저장된 인접한 정점까지의 거리보다 작다면 갱신하고 큐에 넣습니다.
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, (distance, adjacent))
        # 모든 정점까지의 최단 거리를 담은 딕셔너리를 반환합니다.
        return distances
    
    # 각각 따로 택시를 탔을 때의 비용을 구합니다. 시작점에서 A와 B의 목적지까지의 최단 거리를 구하고 요금을 더합니다.
    cost = dijkstra(s)[a] + dijkstra(s)[b]
    # 모든 지점에 대해 합승을 고려해봅니다. 시작점에서 합승 지점까지의 최단 거리와 합승 지점에서 A와 B의 목적지까지의 최단 거리를 구하고 요금을 더합니다.
    for i in range(1, n + 1):
        if s != i: # 시작점과 같은 지점은 제외합니다.
            cost = min(cost, dijkstra(s)[i] + dijkstra(i)[a] + dijkstra(i)[b]) # 기존 비용과 비교하여 최소값을 갱신합니다.
    # 최종 비용을 반환합니다.
    return cost