def solution(triangle):
    answer = 0
    dp = [x.copy() for x in triangle]
    # print(dp)
    
    for r in range(1,len(triangle)):
        for c in range(len(triangle[r])):  # 0, 1, ..., r
            # (r-1, c-1) or (r-1, c) 중에서 max값 선택하면 됨
            ## 맨 왼쪽인 경우
            if c == 0:
                dp[r][c] = dp[r-1][c] + dp[r][c]
            ## 맨 오른쪽인 경우
            elif c == r:
                dp[r][c] = dp[r-1][c-1] + dp[r][c]
            ## 중간인 경우
            else:
                dp[r][c] = max(dp[r-1][c], dp[r-1][c-1]) + dp[r][c]
    
    answer = max(dp[-1])
        
    
    return answer