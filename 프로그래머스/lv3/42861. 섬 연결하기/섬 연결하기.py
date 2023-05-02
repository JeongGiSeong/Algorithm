def solution(n: int, costs: list):

    def find_parent(parent: list, n: int) -> int:
        if parent[n] != n:
            parent[n] = find_parent(parent, parent[n])
        return parent[n]

    def union_parent(parent: list, node_a: int, node_b: int):
        a = find_parent(parent, node_a)
        b = find_parent(parent, node_b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

    parent = [i for i in range(n)]
    answer = 0
    costs.sort(key= lambda x:x[2])

    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer