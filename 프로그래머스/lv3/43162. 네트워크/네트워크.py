def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(idx):
        for i in range(n):
            if i == idx: continue
            if computers[idx][i] and not visited[i]:
                visited[i] = True
                dfs(i)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer