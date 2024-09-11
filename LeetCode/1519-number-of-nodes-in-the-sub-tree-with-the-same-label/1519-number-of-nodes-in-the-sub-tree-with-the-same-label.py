# i번 노드와 하위 트리에 i번 노드와 같은 레이블의 개수
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        result = [0] * n
        
        def dfs(node: int, parent: int) -> Counter:
            counter = Counter()
            counter[labels[node]] += 1
            
            for neighbor in tree[node]:
                # 양방향 트리라 부모 노드를 방문하지 않도록 설정
                if neighbor != parent:
                    counter += dfs(neighbor, node)
            
            result[node] = counter[labels[node]]
            return counter
        
        # 루트 노드(0)부터 DFS 시작
        dfs(0, -1)
        
        return result