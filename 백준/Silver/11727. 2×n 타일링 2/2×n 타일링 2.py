"""
s1 = 1
s2 = s1 + 2
s3 = s2 + s1*2
s4 = s3 + s2*2
"""
n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2
    
print(dp[n]%10007)