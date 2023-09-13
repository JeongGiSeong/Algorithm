import sys

# 플로이드 와샬
def solution(n, s, a, b, fares):
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