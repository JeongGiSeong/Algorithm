def solution(triangle):
    n = len(triangle)
    # 7  0  0  0  0 
    # 10 15 0  0  0
    # 18 16 15 0  0
    # 20 25 20 19 0
    # 24 30 27 26 24
    
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[n-1])