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
            # 덧셈
            dfs(idx + 1, num + numbers[idx])
            # 뺄셈
            dfs(idx + 1, num - numbers[idx])
        
    dfs(0, 0)
    return answer