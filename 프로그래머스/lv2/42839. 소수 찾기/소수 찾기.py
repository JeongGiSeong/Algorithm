import sys

def solution(numbers):
    # 소수 판별 함수
    def is_prime(n):
        if n < 2:  # 2보다 작으면 소수가 아님
            return False
        for i in range(2, int(n**0.5)+1):  # 2부터 해당 숫자의 제곱근까지 반복
            if n % i == 0:  # 나누어 떨어지면 소수가 아님
                return False
        return True  # 나누어 떨어지지 않으면 소수임
    
    num = set()
    # DFS로 완전탐색
    sys.setrecursionlimit(10 ** 6)
    stack = []
    visited = [False] * len(numbers)
    def dfs(depth):
        if depth > 0:
            num.add(int(''.join(map(str, stack))))
        
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                stack.append(numbers[i])  # 수정된 부분
                dfs(depth + 1)
                stack.pop()
                visited[i] = False
    dfs(0)
    
    num = set(filter(lambda x:is_prime(x), num))
        
    return len(num)