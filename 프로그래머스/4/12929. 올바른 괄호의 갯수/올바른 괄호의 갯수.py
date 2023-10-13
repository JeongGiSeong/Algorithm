def solution(n):
    # 카탈란 수를 이용해서 푸는 문제
    # Catalan(n) = 2n! / ( n! * (n+1)! )
    
    # DP (n이 크면 가장 빠름)
    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

    return dp[n]

#########################################################################################################

    # n이 작으면 가장 빠름
    from math import factorial 
    
    return factorial(2*n)/(factorial(n+1)*factorial(n))

#########################################################################################################

    # 재귀 (중복 부분 문제로 인해 제일 오래 걸림)
    # catalan(n, c)로 리스트까지 줘서 메모이제이션을 사용하면 빠름
    def catalan(n, c):
        if c[n] == 0:
            for i in range(n):
                c[n] += catalan(i, c) * catalan(n-i-1, c)
        return c[n]
    
    c = [1] + [0] * n
    return catalan(n, c)
        
        