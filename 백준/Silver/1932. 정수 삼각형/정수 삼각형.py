# 입력받기
N = int(input())
arr = [ [] for _ in range(N+1)]
for i in range(1,N+1):
    arr[i] = [0] + list(map(int,input().split()))
#
# for row in arr:
#     print(row)
#

# dp
dp = [[0]*(i+1) for i in range(0, N+1)]    # 1행에 1개, 2행에 2개 , 3행에 3개,... / dp[r][c]는 r행의 c번째 값 선택시 현재 최대값을 의미
# for row in dp:
#     print(row)
for r in range(1,N+1):
    for c in range(1,r+1): # r행에는 (r,1) , (r,2) , ... (r, r) 위치가 가능함
        if r == 1: # 첫 노드 경우
            dp[r][c] = arr[r][1]

        else:
            if c != 1 and c !=r : # 중간 노드 경우
                dp[r][c] = max(dp[r-1][c-1] ,dp[r-1][c] )  + arr[r][c]  # 왼위, 오위

            elif c == 1: # 맨 왼편 노드 경우
                dp[r][c] = dp[r-1][c] +arr[r][c]

            elif c == r: # 맨 오른편 노드 경우
                dp[r][c] = dp[r-1][c-1] + arr[r][c]

print(max(dp[N]))

