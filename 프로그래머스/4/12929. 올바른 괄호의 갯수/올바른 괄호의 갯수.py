def solution(n):
    # 카탈란 수를 이용해서 푸는 문제
    # Catalan(n) = 2n! / ( n! * (n+1)! )
    
    # DP
    dp = [0 for i in range(n+1)]
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

    return dp[n]

#########################################################################################################

    from math import factorial 
    
    return factorial(2*n)/(factorial(n+1)*factorial(n))

#########################################################################################################

    # 재귀
    def catalan(n):
        if n == 0:
            return 1
        c = 0
        for i in range(n):
            c += catalan(i) * catalan(n-i-1)
        return c
    
    return catalan(n)
        
        