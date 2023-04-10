N = int(input())

arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(int,input().split()))

#
# def dfs(row, col, cur_sum):
#     global max_sum
#
#     if row == N-1:
#         if max_sum < cur_sum:
#             max_sum = cur_sum
#
#     else:
#         dfs(row + 1, col  , cur_sum + arr[row+1][col])
#         dfs(row + 1, col+1, cur_sum + arr[row+1][col+1])
#
#
# max_sum = 0
# dfs(0,0,arr[0][0])
# print(max_sum)
#



dp = [[0]*i for i in range(1,N+1)]

r = 0
while r < N:
    if r == 0:
        dp[r][0] = arr[r][0]

    else:
        for c in range(r+1):  # r번째 row애는 r+1개 col 존재!, 0,1,2,...,r
            if c == 0 :
                dp[r][c] = dp[r-1][c] +  arr[r][c]
            elif c == r :
                dp[r][c] = dp[r-1][c-1] + arr[r][c]

            else: # 0 <c < r
                dp[r][c] = max(dp[r-1][c-1], dp[r-1][c]) + arr[r][c]
    r += 1

print(max(dp[N-1]))