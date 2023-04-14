def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]
    for puddle in puddles:
        c, r = puddle
        dp[r][c] = -1
    
    for r in range(1,n+1):
        for c in range(1,m+1):
            # 1. 처음
            if r == 1 and c == 1:
                dp[r][c] = 1
            
            elif dp[r][c] != -1:
                # 2. 맨윗줄
                if r == 1:
                    if dp[r][c-1] != -1:
                        dp[r][c] += dp[r][c-1]

                # 3. 맨 왼쪽
                elif c == 1:
                    if dp[r-1][c] != -1:
                        dp[r][c] += dp[r-1][c]

                # 4. 그 외
                else:
                    if dp[r][c-1] != -1:
                        dp[r][c] += dp[r][c-1]
                    if dp[r-1][c] != -1:
                        dp[r][c] += dp[r-1][c]
                
    # print(dp[n][m])
    # for row in dp:
    #     print(row)

    answer = dp[n][m] % 1000000007

    return answer