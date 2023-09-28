def solution(info, edges):
    visited = [0] * len(info)
    answer = [] # 가능한 경우들 중에서 양의 최대 개수를 저장하는 리스트
    
    def dfs(sheep, wolf):
        if sheep > wolf: # 양의 수가 늑대의 수보다 많으면
            answer.append(sheep) # 그 때의 양의 수를 answer에 추가
        else:
            return
        
        for p, c in edges: 
            if visited[p] and not visited[c]: 
                visited[c] = 1
                if info[c] == 0: 
                    dfs(sheep+1, wolf)  # 다음 노드가 양인 경우
                else:
                    dfs(sheep, wolf+1)  # 다음 노드가 늑대인 경우
                visited[c] = 0   # 현재 노드에 대한 탐색이 종료되면 방문 여부를 원상 복구

	# 탐색 시작
    visited[0] = 1  
    dfs(1, 0)

    return max(answer)
