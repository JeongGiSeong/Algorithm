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
        # {c : {d : f}}
        graph[c][d] = f
        graph[d][c] = f
    
    def dijkstra(start):
        distances = {node: float('INF') for node in graph}
        distances[start] = 0
        queue = []
        # heapq로 우선순위 큐 구현
        heapq.heappush(queue, (0, start))
        while queue:
            # 우선순위 큐 -> 가장 적은 요금과 그 정점이 pop
            current_distance, current_node = heapq.heappop(queue)
            # 현재 정점까지의 요금이 이미 저장된 요금보다 크다면 무시
            if distances[current_node] < current_distance:
                continue
            # 현재 정점과 인접한 정점들에 대해 반복.
            for adjacent, weight in graph[current_node].items():
                # 현재 정점까지의 거리와 인접한 정점까지의 요금을 더합니다.
                distance = current_distance + weight
                # 이 값이 기존에 저장된 인접한 정점까지의 거리보다 작다면 갱신하고 큐에 넣습니다.
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, (distance, adjacent))
        return distances
    
    # 각각 따로 택시를 탔을 때의 비용
    s_result = dijkstra(s)
    cost = s_result[a] + s_result[b]
    # 합승 고려
    for i in range(1, n + 1):
        if s != i: # 시작점 제외
            i_result = dijkstra(i)
            cost = min(cost, s_result[i] + i_result[a] + i_result[b]) # 기존 비용과 비교하여 최소값을 갱신
    return cost