import sys
from collections import deque as dq
input = sys.stdin.readline

vertex_num = int(input())
edge_list = [list(map(int, input().split())) for __ in range(vertex_num-1)]
solution = list(map(int, input().split()))


def make_graph(vertex_num, edge_list):
    graph = {}
    for i in range(1, vertex_num+1):
        graph[i] = []
    for edge in edge_list:
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph


def make_ordered_graph(graph, solution):
    ordered_graph = graph.copy()
    order = [0] * (vertex_num+1)

    for i in range(len(solution)):
        order[solution[i]] = i
    for i in range(1, len(graph)+1):
        ordered_graph[i].sort(key=lambda x: order[x])

    return ordered_graph


def BFS(graph):
    que = dq()
    visited = [0] * (vertex_num+1)

    que.append(1)
    visited[1] = 1
    path = [1]

    while que:
        basev = que.popleft()
        for nextv in graph[basev]:
            if visited[nextv] == 0:
                que.append(nextv)
                visited[nextv] = 1
                path.append(nextv)

    return path


graph = make_graph(vertex_num, edge_list)
ordered_graph = make_ordered_graph(graph, solution)
path = BFS(ordered_graph)

if path == solution:
    print(1)
else:
    print(0)