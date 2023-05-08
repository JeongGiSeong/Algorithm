def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, num):
        nonlocal answer
        
        if idx == n:
            if num == target:
                answer += 1
            return
         
        else:
            # 덧셈. 남은 수를 전부 더해도 target보다 작거나 
            if num + sum(numbers[idx:]) >= target:
                dfs(idx + 1, num + numbers[idx])
            # 뺄셈. 남은 수를 전부 빼도 target보다 크거나
            if num - sum(numbers[idx:]) <= target:
                dfs(idx + 1, num - numbers[idx])
        
    dfs(0, 0)
    return answer