"""
1. n = 1
a1 = 1

2. n = 2 : 00, 11
a2 =  a1 + 1

3. n = 3 : 001, ,111, 100
a3 = a2 + a1
"""

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] %= 15746

print(dp[n])