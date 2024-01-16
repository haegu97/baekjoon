n = int(input())
dp = [i for i in range(n+1)]

for i in range(n+1):
    dp[i] = dp[i-1] + dp[i]
print(dp[n-1])